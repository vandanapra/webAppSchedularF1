from django.db import models
from datetime import datetime

# Create your models here.
class Detail(models.Model):
    operatorname=models.CharField(max_length=122)
    identity=models.CharField(max_length=122)
    machine=models.CharField(max_length=122)
    variant=models.CharField(max_length=122)
    partname=models.CharField(max_length=122)
    partno=models.CharField(max_length=122)
    timein=models.DateTimeField(null=True)
    timeout=models.DateTimeField(null=True)
    date=models.DateField()
