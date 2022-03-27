from django.db import models
from datetime import datetime

from matplotlib.style import available

# Create your models here.
class inhouseInventory(models.Model):
    sno=models.IntegerField(primary_key=True,default=0)
    productSno=models.CharField(max_length=122,default=0)
    level=models.CharField(max_length=122,default=0)
    qpp=models.CharField(max_length=122,default=0)
    dimension=models.CharField(max_length=122,default=0)
    drawingno=models.CharField(max_length=122,default=0)
    availableNos=models.CharField(max_length=122,default=0)
    description=models.DateTimeField(null=True)
    timein=models.DateTimeField(null=True)
    date=models.DateField()
