

import logging
from src.simulator.machine import SimulatedMachine

logger = logging.getLogger("factory")


class SimulatedFactory(object):
    def __init__(self, infrastructure):
        self._infrastructure = infrastructure
        self._machines = None
        self._inventory = []

    @property
    def machines(self):
        if not self._machines:
            self._machines = [SimulatedMachine(**machine)
                              for machine in self._infrastructure.machine_list]
        return self._machines

    @property
    def lines(self):
        return self._infrastructure.lines_list

    @property
    def variants(self):
        return self._infrastructure.variants_list

    @property
    def inventory(self):
        return self._inventory
