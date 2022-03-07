

import logging
from src.simulator.component import SimulatedComponent

logger = logging.getLogger("machine")


class SimulatedMachine(object):
    def __init__(self, name, line, machine_no, status, operation):
        # TODO : What does Operation have to do with Machine?
        self.name = name
        self.line = line
        self.machine_no = machine_no
        self.status = status
        self.available = True
        self.operation = operation

    """Start delivery of required components to a machine and start the operation"""
    def distribution_and_operation(self, operation, components_list, agent):
        # while done_in:
        #   print("delivery started")
        # logger.debug("Executing '{}' at '{}'".format(operation['name'], self.name))
        yield agent.env.timeout(0)
        agent.env.process(self.start_operation(operation, components_list, agent))

    """Start the operation on a Machine"""
    def start_operation(self, operation, components, agent):
        if self.status == "READY":
            print("*******************************************************")
            print("*****************Something went wrong.*****************")
            print("*******************************************************")
            print(self.name, self.status)
            return
        # self.status = "NOT READY"
        proc_t = operation["time"][components[0].coach_variant]
        done_in = proc_t
        data = dict()
        while done_in:
            start = agent.env.now
            data["Operation"] = operation["name"]
            data["Machine"] = self.name
            data["Coach Variant"] = components[0].coach_variant
            data["Start Time"] = agent.convert_to_date(start*60)
            data["Input"] = []
            for item in components:
                data["Input"].append(item.name)
            # print("started processing %s on machine %s at %s"%(operation["name"],self.name,start))
            yield agent.env.timeout(done_in)
            # self.part_being_proc = None
            self.available = True
            self.status = "READY"
            # print("Completed the process step of %s on machine %s at %s and output %s sent to
            # "next machine."%(operation["name"], self.name, env.now,operation["outputs"]))
            done_in = 0
        variant = components[0].coach_variant
        priority = components[0].priority
        comp_no = components[0].component_no
        line = components[0].line
        data["Output"] = []
        data["End Time"] = agent.convert_to_date(agent.env.now*60)
        for item in operation["outputs"]:
            if item["name"] == "Coach":
                data["Output"].append("Coach")
                agent.completed_orders[variant] += 1
                break
            if item in operation["inputs"]:
                for comp in components:
                    if comp.name == item["name"] and comp.component_no == item["part_no"] and comp.assembly_code == item["assembly_code"]:
                        comp_tup = (item["name"], item["part_no"], item["assembly_code"])
                        # print(comp_tup)
                        new_comp = SimulatedComponent(
                            comp.name, comp.coach_variant, comp.priority,
                            comp.line, comp.component_no,
                            agent.process_flow[comp.line][comp_tup][0]["route"][comp.seq+1],
                            "READY", comp.seq+1, comp.assembly_code, ""
                        )
                        data["Output"].append(new_comp.name)
                        components.remove(comp)
                        del comp
                        agent.factory.inventory.append(new_comp)
            else:
                comp_tup = (item["name"], item["part_no"], item["assembly_code"])
                if comp_tup not in agent.process_flow[line]:
                    # completed_order[variant]+=1
                    # break
                    # print(comp_tup)
                    if comp_tup in agent.process_flow["sh"]:
                        line = "sh"
                    else:
                        print("some problem with changing line")
                        exit()
                new_comp = SimulatedComponent(
                    comp_tup[0], variant, priority,
                    line, comp_tup[1],
                    agent.process_flow[line][comp_tup][0]["route"][0],
                    "READY", 0, comp_tup[2], ""
                )
                data["Output"].append(new_comp.name)
                agent.factory.inventory.append(new_comp)
        for comp in components:
            del comp
        data["Coach Variant Manufactured"] = agent.completed_orders[variant]
        agent.schedule.append(data)

    def __repr__(self):
        return "<{} {} {}>".format(self.__class__.__name__, self.line, self.name, self.status)