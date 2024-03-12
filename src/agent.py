
import simpy
import time
from datetime import datetime
from src.simulator.factory import SimulatedFactory
from src.simulator.component import SimulatedComponent
from order.models import productionOrder

import logging
logger = logging.getLogger("agent")


class OrderSimulationComplete(Exception):
    pass


class SchedulingAgent(object):
    def __init__(self, factory: SimulatedFactory, process_flow, operations):
        self._factory = factory
        self._process_flow = process_flow
        self._operations = operations
        self._orders = []
        self._schedule = []
        self._completed_orders = None
        self._env = None
        self._timestamp = None
        self._earliest_start_date = None

    @property
    def env(self):
        if not self._env:
            logger.info("Creating the Virtual Environment")
            self._env = simpy.Environment()
        return self._env

    @property
    def schedule(self):
        return self._schedule

    @property
    def process_flow(self):
        return self._process_flow

    @property
    def factory(self):
        return self._factory

    def create_order(self,order_id, order_variant, order_qty,
                     order_priority, order_start_date):
        self._orders.append(
            {order_variant:
                {'id':order_id,
                 'qty': order_qty,
                 'priority': order_priority,
                 'start_date': order_start_date}
             }
        )

    @property
    def completed_orders(self):
        if not self._completed_orders:
            logger.info("Creating an object to store completed orders")
            self._completed_orders = {variant: 0 for variant in self._factory.variants}
        return self._completed_orders

    @property
    def earliest_start_date(self):
        if not self._earliest_start_date:
            logger.info("Determining the earliest possible start date")
            earliest_start_date = None
            min_time_step = 10e10
            for order in self._orders:
                for variant in order.keys():
                    if order[variant]["start_date"] == "":
                        continue
                    if time.mktime(datetime.strptime(order[variant]["start_date"], "%Y-%m-%d").timetuple()) < min_time_step:
                        min_time_step = time.mktime(datetime.strptime(order[variant]["start_date"], "%Y-%m-%d").timetuple())
                        earliest_start_date = order[variant]["start_date"]
            self._earliest_start_date = earliest_start_date
        return self._earliest_start_date

    def prep(self):
        logger.info("Initialize all the input components to start manufacturing operations")
        for order in self._orders:
            for variant in order.keys():
                for i in range(order[variant]["qty"]):
                    for line in self._process_flow.keys():
                        for comp_tup in self._process_flow[line]:
                            if str(comp_tup[2]).islower():
                                for temp in self._process_flow[line][comp_tup]:
                                    for j in range(temp["qpc"]):
                                        new_comp = SimulatedComponent(
                                            comp_tup[0], variant,
                                            order[variant]["priority"],
                                            line, comp_tup[1],
                                            self._process_flow[line][comp_tup][0]["route"][0],
                                            "READY", 0, comp_tup[2],
                                            order[variant]["start_date"])
                                        self._factory.inventory.append(new_comp)
        # from itertools import product

        # for order, variant, i, line, comp_tup, temp, j in product(
        #     self._orders,
        #     (key for key in order.keys()),
        #     range(order[variant]["qty"]),
        #     (key for key in self._process_flow.keys()),
        #     (comp_tup for comp_tup in self._process_flow[line] if str(comp_tup[2]).islower()),
        #     (temp for temp in self._process_flow[line][comp_tup]),
        #     range(temp["qpc"])
        # ):
        #     new_comp = SimulatedComponent(
        #         comp_tup[0], variant,
        #         order[variant]["priority"],
        #         line, comp_tup[1],
        #         self._process_flow[line][comp_tup][0]["route"][0],
        #         "READY", 0, comp_tup[2],
        #         order[variant]["start_date"]
        #     )
        #     self._factory.inventory.append(new_comp)


    @property
    def order_completed(self):
        for order in self._orders:
            for variant in order.keys():
                if order[variant]["qty"] != self.completed_orders[variant]:
                    return False
                order = productionOrder.objects.get(orderId=order[variant]["id"],status='pending')
                order.status = 'completed'
                order.save()
        return True

    def step(self):
        if self.order_completed:
            raise OrderSimulationComplete()

        # for line in self._factory.lines:
        #     for machine in self._factory.machines:
        #         if machine.line.lower() == line.lower() and machine.status == "READY":
        #             for priority in range(1, 11):
        #                 if machine.status == "READY":
        #                     # logger.debug("EXEC STEP {}:{}".format(line, machine))
        #                     input_components = self._operations[machine.operation]["inputs"]
        #                     for variant in self._factory.variants:
        #                         if machine.status == "READY":
        #                             self.check_start_operation(
        #                                 self._operations[machine.operation],
        #                                 priority, machine, input_components, line, variant)
        for line in self._factory.lines:
            for machine in [m for m in self._factory.machines if m.line.lower() == line.lower() and m.status.startswith('running')]:
                for priority in range(1, 11):
                    if machine.status.startswith('running'):
                        input_components = self._operations[machine.operation]["inputs"]
                        for variant in [v for v in self._factory.variants if machine.status.startswith('running')]:
                            self.check_start_operation(
                                self._operations[machine.operation],
                                priority, machine, input_components, line, variant)

        self.env.step()

    def execute(self):
        logger.info("Got earliest_start_date: {}".format(self.earliest_start_date))
        self.prep()
        self._timestamp = time.mktime(datetime.strptime(self.earliest_start_date, "%Y-%m-%d").timetuple())
        while True:
            try:
                self.step()
            except OrderSimulationComplete:
                break

    def check_start_operation(self, operation, priority, machine, input_components, line, variant):
        components_list = []
        for component in input_components:
            for item in self._factory.inventory:
                if item.line == line and \
                        (item.machine == machine.name or machine.name in item.machine) and \
                        item.name == component["name"] and \
                        item.component_no == component["part_no"] and \
                        item.priority == priority and item.coach_variant == variant and \
                        (item.start_date == "" or self.convert_to_timesteps(item.start_date) <= self.env.now):
                    components_list.append(item)
                    break
        if len(input_components) == len(components_list):
            for item in components_list:
                self._factory.inventory.remove(item)
            machine.status = "NOT READY"
            self.env.process(machine.distribution_and_operation(operation, components_list, self))

    def convert_to_timesteps(self, date):
        end = time.mktime(datetime.strptime(date, "%Y-%m-%d").timetuple())
        start = time.mktime(datetime.strptime(self.earliest_start_date, "%Y-%m-%d").timetuple())
        return (end - start) / 60

    def convert_to_date(self, timesteps):
        timestamps = self._timestamp + timesteps
        return datetime.fromtimestamp(timestamps).strftime("%Y-%m-%d %H:%M:%S")

    @property
    def title(self):
        title = ''
        # for order in self._orders:
        #     for variant in order.keys():
        #         if order[variant]["qty"] > 0:
        #             title += variant + ": " + " Quantity: " + str(order[variant]["qty"]) + " Priority: " + str(
        #                 order[variant]["priority"]) + " Start Date: " + order[variant]["start_date"] + "<br>"
        return title
