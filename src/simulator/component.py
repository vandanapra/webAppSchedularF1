

class SimulatedComponent(object):
    def __init__(self, name, coach_variant, priority, line, component_no,
                 machine, status, seq, assembly_code, start_date):
        self.name = name
        self.coach_variant = coach_variant
        self.priority = priority
        self.line = line
        self.component_no = component_no
        self.machine = machine
        self.status = status
        self.seq = seq
        self.assembly_code = assembly_code
        self.start_date = start_date
