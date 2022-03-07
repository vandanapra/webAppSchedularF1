

from src.inputs.dataset import VariantDataSet
from src.inputs.mcf import mcf


ac3t = VariantDataSet(
    lines_list=mcf.lines_list,
    process_flows={
        'swl': ('operation_data.xlsx', 'swl_process_flow'),
        'ewl': ('operation_data.xlsx', 'ewl_process_flow'),
        'rf': ('operation_data.xlsx', 'rf_process_flow'),
        'uf': ('operation_data.xlsx', 'uf_process_flow'),
        'sh': ('operation_data.xlsx', 'sh_process_flow'),
    },
    operations={
        'swl': ('operation_data.xlsx', 'swl_operation_components'),
        'ewl': ('operation_data.xlsx', 'ewl_operation_components'),
        'rf': ('operation_data.xlsx', 'rf_operation_components'),
        'uf': ('operation_data.xlsx', 'uf_operation_components'),
        'sh': ('operation_data.xlsx', 'sh_operation_components'),
    },
    operation_details={
        'swl': ('operation_data.xlsx', 'swl_operation_details'),
        'ewl': ('operation_data.xlsx', 'ewl_operation_details'),
        'rf': ('operation_data.xlsx', 'rf_operation_details'),
        'uf': ('operation_data.xlsx', 'uf_operation_details'),
        'sh': ('operation_data.xlsx', 'sh_operation_details'),
    },
    machine_operation_time_details ={
        'swl': ('manufacturing_data_all_variants.xlsx', 'UF'),
        'ewl': ('manufacturing_data_all_variants.xlsx', 'EW'),
        'rf': ('manufacturing_data_all_variants.xlsx', 'SW'),
        'uf': ('manufacturing_data_all_variants.xlsx', 'RF'),
        'sh': ('manufacturing_data_all_variants.xlsx', 'Shell_assembly'),

    }
)
