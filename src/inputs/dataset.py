import os
import pandas
import random
import logging
from machines.models import Machine
logger = logging.getLogger("dataset")

_inputs_path = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    os.pardir, '_input')
)


class InfrastructureDataSet(object):
    def __init__(self, location_code, location_name,
                 machine_list, machine_list_format):
        self._location_code = location_code
        self._location_name = location_name

        self._machine_list_format = machine_list_format or 'csv'
        self._machine_list_source = machine_list
        self._machine_list = None

    def _machines_reader_csv(self):
        actual_path = os.path.join(_inputs_path, self._machine_list_source)
        logger.info("Loading Machine List from {}".format(actual_path))
        _machines_raw = pandas.read_csv(actual_path)
        _machines = []
        for index, row in _machines_raw.iterrows():
            d = {"name": row[0],
                 "line": row[1],
                 "machine_no": row[2],
                 "status": row[3],
                 "operation": row[4]}
            _machines.append(d)
        return _machines
    
    def _machines_reader_db(self):
        logger.info("Loading Machine List from {}".format(Machine))
        _machines_raw = Machine.objects.all()
        _machines = []
        for row in _machines_raw:
            d = {"name": row.name,
                 "line": row.line,
                 "machine_no": row.machine_no,
                 "status": row.status,
                 "operation": row.operation}
            _machines.append(d)
            # logger.info("Machine List: {}".format(d))
        return _machines

    _machine_list_readers = {
        'csv': _machines_reader_csv,
        'db':_machines_reader_db,
    }

    @property
    def machine_list(self):
        if not self._machine_list:
            readfunc = self._machine_list_readers[self._machine_list_format]
            logger.info("Machine List: {}".format(readfunc))
            self._machine_list = readfunc(self)
        return self._machine_list

    @property
    def lines_list(self):
        return ['swl', 'ewl', 'rf', 'uf', 'sh']

    @property
    def variants_list(self):
        return ["LWSCZAC (2nd Class AC Chair Car)" ,
                "LWFCZAC (Executive Class AC Chair Car)" ,
                "LWACCN (AC-3 tier)" ,
                "HUMSAFAR (AC-3Tier)" ,
                "LWACCW (AC-2 Tier)",
                "LWSCN (Non-AC Sleeper)",
                "LS (GS/EOG 100 SEATER)",
                "LWSDD (Deendayalu)",
                "LWS (Antyodaya Coach)",
                "LWLRRM (450KVA Power Car)",
                "LWLRRM (750KVA Power Car)",
                "LDSLR (Under Slung Luggage Cum brake Van)",
                "LSLRD with DA set (Luggage Cum brake van)",
                "LWCBAC (AC Buffet Car)",
                "LWSCZ (2nd Class Non-AC Chair Car)",
                "TRC (AC Track recording Car)",
                "TRSC (AC track recording staff Car)",
                "LWFAC (AC 1st Class)",
                "LFCWAC Composite (FAC+AC2T)",
                "LVPH (LHB Parcel Van)",
                "LWACCNE (Gareeb Rath AC Sleeper Coach)",
                "LWS-AC (AC- General)"
            ]


class VariantDataSet(object):
    def __init__(self, lines_list, process_flows, operations, operation_details,machine_operation_time_details):
        self._process_flow_files = process_flows
        self._operations_files = operations
        self._operation_details_files = operation_details
        self._lines_list = lines_list
        self._machine_operation_time_details_files = machine_operation_time_details

        self._line_process_flow = {}
        self._process_flow = {}

        self._line_operations = {}
        self._operations = {}

        self._line_operation_details = {}
        self._operation_details = {}
        self._machine_operation_time_details = {}

    @property
    def line_process_flow(self):
        if not self._line_process_flow:
            for line in self._lines_list:
                fname, sheet = self._process_flow_files[line]
                fpath = os.path.join(_inputs_path, fname)
                logger.info("Loading Line Process Flow from {}:{}".format(fpath, sheet))
                self._line_process_flow[line] = pandas.read_excel(
                    fpath, sheet_name=sheet, header=None, skiprows=[0],engine="openpyxl"
                )
        return self._line_process_flow

    @property
    def process_flow(self):
        if not self._process_flow:
            for line in self._lines_list:
                pf = self.line_process_flow[line]
                process_d = {}
                columns = list(pf)
                for index, row in pf.iterrows():
                    comp_no = row[2]
                    if pandas.isnull(comp_no):
                        comp_no = 0
                    ac = str(row[0])
                    if pandas.isnull(ac):
                        ac = "Z"
                    if '=' in str(ac):
                        ac = ac[ac.index("=") + 1:]
                    p = (row[1], comp_no, ac)
                    if p in process_d:
                        # TODO What is this?
                        # print(p)
                        pass
                    if not pandas.isnull(row[1]) and p not in process_d:
                        process_d[p] = []

                    temp = {"route": [], "qpc": row[3]}
                    for i in range(4, len(columns)):
                        if not pandas.isnull(row[i]):
                            temp["route"].append(row[i])
                            # temp["route"].append(row[i])
                    process_d[p].append(temp)
                d = {line: process_d}
                self._process_flow.update(d)
        return self._process_flow

    @property
    def line_operations(self):
        if not self._line_operations:
            for line in self._lines_list:
                fname, sheet = self._operations_files[line]
                fpath = os.path.join(_inputs_path, fname)
                logger.info("Loading Line Operations from {}:{}".format(fpath, sheet))
                self._line_operations[line] = pandas.read_excel(
                    fpath, sheet_name=sheet, header=None, skiprows=[0],engine="openpyxl"
                )
        return self._line_operations

    @property
    def all_operations(self):
        return [self.line_operations[line] for line in self._lines_list]

    @property
    def operations(self):
        if not self._operations:
            for line in self._lines_list:
                op = self.line_operations[line]
                for index, row in op.iterrows():
                    # print(row[0], row[1], row[2], row[3], row[4])
                    if pandas.isnull(row[0]):
                        continue
                    if row[0] not in self._operations:
                        self._operations[row[0]] = {}
                        self._operations[row[0]]["name"] = row[0]
                    self._operations[row[0]].setdefault("inputs", [])
                    self._operations[row[0]].setdefault("outputs", [])

                    if row[4] == "I":
                        ac = str(row[5])
                        if pandas.isnull(row[5]):
                            ac = "Z"
                        if '=' in str(ac):
                            ac = ac[0:ac.index("=")]
                        self._operations[row[0]]["inputs"].append({
                            "name": row[1],
                            "part_no": 0 if pandas.isnull(row[2]) else row[2],
                            "qpc": row[3],
                            "assembly_code": ac
                        })

                    elif row[4] == "O":
                        ac = str(row[5])
                        if pandas.isnull(row[5]):
                            ac = "Z"
                        if '=' in str(ac):
                            ac = ac[0:ac.index("=")]
                        self._operations[row[0]]["outputs"].append({
                            "name": row[1],
                            "part_no": 0 if pandas.isnull(row[2]) else row[2],
                            "qpc": row[3],
                            "assembly_code": ac
                        })
            self._inject_operation_details()
        return self._operations

    @property
    def line_operation_details(self):
        if not self._line_operation_details:
            for line in self._lines_list:
                fname, sheet = self._operation_details_files[line]
                fpath = os.path.join(_inputs_path, fname)
                logger.info("Loading Line Operation Details from {}:{}".format(fpath, sheet))
                self._line_operation_details[line] = pandas.read_excel(
                    fpath, sheet_name=sheet, header=None, skiprows=[0],engine="openpyxl"
                )
        return self._line_operation_details
    
    @property
    def machine_operation_time_details(self):
        if not self._machine_operation_time_details:
            for line in self._lines_list:
                fname, sheet = self._machine_operation_time_details_files[line]
                fpath = os.path.join(_inputs_path, fname)
                logger.info("Loading Line Operation Details from {}:{}".format(fpath, sheet))
                self._machine_operation_time_details[line] = pandas.read_excel(
                    fpath, sheet_name=sheet, header=None, skiprows=[0],engine="openpyxl"
                )
        return self._machine_operation_time_details
    
    # @staticmethod
    # def jitter_time(time, percent_bounds=0.2):
    #     start = int(time - percent_bounds * time)
    #     end = int(time + percent_bounds * time)
    #     return random.randint(max(1, start), end)

    def _inject_operation_details(self):
        for line, op_details in self.machine_operation_time_details.items():
            for index, row in op_details.iterrows():
                if pandas.isnull(row[0]):
                    continue
                if row[0] not in self._operations:
                    self._operations[row[0]]= {}
                else:
                    #self._operations[row[0]]["name"] = row[0]
                    self._operations[row[0]]["machine"] = []
                    if "&" in row[1]:
                        self._operations[row[0]]["machine"] = row[1].split(" & ")
                    else:
                        self._operations[row[0]]["machine"].append(row[1])
                    self._operations[row[0]]["time"] = dict()
                    self._operations[row[0]]["time"]["LWSCZAC (2nd Class AC Chair Car)"] = row[2]
                    self._operations[row[0]]["time"]["LWFCZAC (Executive Class AC Chair Car)"] = row[3]
                    self._operations[row[0]]["time"]["LWACCN (AC-3 tier)"] = row[4]
                    self._operations[row[0]]["time"]["HUMSAFAR (AC-3Tier)"] = row[5]
                    self._operations[row[0]]["time"]["LWACCW (AC-2 Tier)"] = row[6]
                    self._operations[row[0]]["time"]["LWSCN (Non-AC Sleeper)"] = row[7]
                    self._operations[row[0]]["time"]["LS (GS/EOG 100 SEATER)"] = row[8]
                    self._operations[row[0]]["time"]["LWSDD (Deendayalu)"] = row[9]
                    self._operations[row[0]]["time"]["LWS (Antyodaya Coach)"] = row[10]
                    self._operations[row[0]]["time"]["LWLRRM (450KVA Power Car)"] = row[11]
                    self._operations[row[0]]["time"]["LWLRRM (750KVA Power Car)"] = row[12]
                    self._operations[row[0]]["time"]["LDSLR (Under Slung Luggage Cum brake Van)"] = row[13]
                    self._operations[row[0]]["time"]["LSLRD with DA set (Luggage Cum brake van)"] = row[14]
                    self._operations[row[0]]["time"]["LWCBAC (AC Buffet Car)"] = row[15]
                    self._operations[row[0]]["time"]["LWSCZ (2nd Class Non-AC Chair Car)"] = row[16]
                    self._operations[row[0]]["time"]["TRC (AC Track recording Car)"] = row[17]
                    self._operations[row[0]]["time"]["TRSC (AC track recording staff Car)"] = row[18]
                    self._operations[row[0]]["time"]["LWFAC (AC 1st Class)"] = row[19]
                    self._operations[row[0]]["time"]["LFCWAC Composite (FAC+AC2T)"] = row[20]
                    self._operations[row[0]]["time"]["LVPH (LHB Parcel Van)"] = row[21]
                    self._operations[row[0]]["time"]["LWACCNE (Gareeb Rath AC Sleeper Coach)"] = row[22]
                    self._operations[row[0]]["time"]["LWS-AC (AC- General)"] = row[23]


#         print(self._operations)
    
# VariantDataSet._inject_operation_details(Self)