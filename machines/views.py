from django.shortcuts import render,HttpResponse
import pandas as pd
from .models import Machine
from operations.models import Operation
from products.models import Product
import os


# Create your views here.
def write_to_model(request):
    machine = pd.read_csv(os.path.join(os.getcwd(),'src/_input/machine.csv'))
    for k,v in machine.iterrows():
        machine = Machine(name=v[0],line=v[1],machine_no=v[2],status=v[3],operation=v[4])
        machine.save()
    
    return HttpResponse('completed')


def write_to_model_operation(request):
    operation = pd.read_excel(os.path.join(os.getcwd(),'src/_input/operation_data.xlsx'),sheet_name='sh_operation_details')
    for k,v in operation.iterrows():
        try:
            if len(v[1].split(',')) > 0:
       
                operation = Operation(name=v[0],time=v[2])
                operation.save()
                for i in v[1].split(','):
                    machine = Machine.objects.get(name=i)
                    operation.machine.add(machine)
        except:
            print(v[1])

    
    return HttpResponse('completed')

def write_to_model_products(request):
    products = pd.read_excel(os.path.join(os.getcwd(),'src/_input/AC-3T_SW_process final.xlsx'),sheet_name='products_list')
    for k,v in products.iterrows():
        try:
            # if len(v[1].split(',')) > 0:
       
                # operation = Operation(name=v[0],time=v[2])
                # operation.save()
                # for i in v[1].split(','):
                #     machine = Machine.objects.get(name=i)
                #     operation.machine.add(machine)
            product = Product(assembly_code=v[0],item=v[1],drg_no=v[2])
            product.save()
        except:
            print(v)

    
    return HttpResponse('completed')
