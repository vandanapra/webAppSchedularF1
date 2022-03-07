

import os
import logging
from pprint import PrettyPrinter
from src.simulator.factory import SimulatedFactory
from src.agent import SchedulingAgent
from src.inputs.mcf import mcf
from src.inputs.ac3t import ac3t
from src.outputs import gantt_chart
from src.outputs import operations_csv
import pymongo
import json

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("agent")
pp = PrettyPrinter().pprint

_outputs_path = "templates"

def main(request,orders):
	logger.info("Creating the Virtual Factory")
	factory = SimulatedFactory(mcf)
	machines = factory.machines
	lines = factory.lines
	process_flow = ac3t.process_flow
	operations = ac3t.operations
	
	logger.info("Creating the Scheduling Agent")
	agent = SchedulingAgent(factory, process_flow, operations)
	
	logger.info("Creating orders for different Coach Variants")
	if len(orders) > 0:
		for order in orders:
			agent.create_order(order.orderVariant,int(order.orderQuantity),int(order.orderPriority),str(order.orderStartDate))
	
	logger.info("Executing the Main Scheduler Algorithm")
	agent.execute()
	
	logger.info("Main Scheduler Algorithm Execution Complete")
	print(agent.completed_orders)
	
	logger.info("Generating Schedule Outputs")
	os.makedirs(_outputs_path, exist_ok=True)
	operations_csv.generate(agent, _outputs_path)
	gantt_chart.generate(request,agent, _outputs_path)
