from django.shortcuts import render
from datetime import datetime
from HMI.models import Detail
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def hmi(request):
    # python_list  = []
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
        # python_list.append(detail)
        # print(python_list)
    messages.success(request, 'your message has been sent!')

    return render(request,"hmi.html")