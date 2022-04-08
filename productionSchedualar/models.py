# Create your models here.
from pickle import TRUE
from pyexpat import model
from django import forms
from django.db import models
from datetime import datetime
from django.forms import ModelForm
from django import forms

class productionOrder(models.Model):
    sno=models.IntegerField(primary_key=TRUE)
    orderRefNo = models.CharField(max_length=122)
    orderVariant = models.CharField(max_length=122)
    orderStartDate = models.DateField(null=True)
    orderEndDate = models.DateField(null=True)
    orderQuantity = models.CharField(max_length=122)
    orderPriority = models.CharField(max_length=122)
    currentDate = models.DateField()

class machineDetails(models.Model):
    machine_name=models.CharField(max_length=122)
    Manufacturer=models.CharField(max_length=122)  
    shopName=models.CharField(max_length=122)  
    MachineNo=models.CharField(max_length=122)
    Description=models.CharField(max_length=122,default=0)
    remarks=models.CharField(max_length=122,default=0)
    currentDate = models.DateField()
