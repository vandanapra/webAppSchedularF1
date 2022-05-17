#import libraries
from unicodedata import name
from django.shortcuts import render,HttpResponse,redirect
from datetime import date, datetime
import json
from matplotlib.font_manager import json_load
from productionSchedualar.models import machineDetails, productionOrder,componentDetails,operationsDetails
from django.contrib import messages


#get orders data here
class FactoryEnvironment():
    def __init__(self):
        self.orders = []
        self.components = []

    def getOrders(self):
        self.orders = productionOrder.objects.all()
        print(self.orders.orderVariant)

    def getComponentsForSpecificOrder(self):
        self.components = componentDetails.objects.all().filter(modelname = self.orders.orderVariant)



if __name__ == '__main__':
    FactoryEnvironment.getOrders()