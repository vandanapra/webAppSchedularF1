

from src.inputs.dataset import InfrastructureDataSet


mcf = InfrastructureDataSet('MCF', "Modern Coach Factory",
                            machine_list="machine.csv",
                            machine_list_format='csv')
