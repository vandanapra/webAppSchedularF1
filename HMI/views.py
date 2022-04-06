from django.shortcuts import render
from datetime import datetime
from HMI.models import Detail
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
import sys
import requests
import json

apiURL = "http://172.26.98.238:8000/hmiPartInfo/"

@csrf_protect
def hmi(request):
    if request.method == "POST":
        operatorname=request.POST.get('operatorname')
        identity=request.POST.get('identity')
        machine=request.POST.get('machine')
        variant=request.POST.get('variant')
        partname=request.POST.get('partname')
        partno=request.POST.get('partno')
        timein=request.POST.get('timein')
        timeout=request.POST.get('timeout')
        detail=Detail(operatorname=operatorname,identity=identity,timein=timein,timeout=timeout,machine=machine,variant=variant,partname=partname,partno=partno,date=datetime.today())
        detail.save()
        doc ={"operatorName":operatorname,"operatorIDNo":identity,"machineName":machine,"variantName":variant,"partName":partname,"partNumber":partno,"timeIN":timein,"timeOUT":timeout}
        jsonConvert = json.dumps(doc)
        createToAPI = requests.post(apiURL,data=jsonConvert)
    messages.success(request, 'your message has been sent!')
    return render(request,"hmi/hmi.html")