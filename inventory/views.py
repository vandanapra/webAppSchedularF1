from django.shortcuts import render,redirect
from datetime import datetime
from inventory.models import inhouseInventory
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
import sys
import requests
import json

apiURL = "http://172.29.96.106:8100/inhouseInventoryInfo/"

@csrf_protect
def inventory(request):
    if request.method == "POST":
        productSno=request.POST.get('productSno')
        level=request.POST.get('level')
        qpp=request.POST.get('qpp')
        dimension=request.POST.get('dimension')
        drawingno=request.POST.get('drawingno')
        availableNos=request.POST.get('availableNos')
        description=request.POST.get('description')
        timein=request.POST.get('timein')
        inhouseInv=inhouseInventory(productSno=productSno,level=level,qpp=qpp,dimension=dimension,drawingno=drawingno,availableNos=availableNos,description=description,timein=timein,date=datetime.today())
        inhouseInv.save()
        doc ={"ProductSNo":productSno,"Level":level,"DrawingNo":drawingno,"Description":description,"qpc":qpp,"length":dimension,"width":dimension,"thick":dimension,"InnerDia":dimension,"OuterDia":dimension,"quantityAvailable":availableNos}
        # mycol.insert_one(doc)
        jsonConvert = json.dumps(doc)
        createToAPI = requests.post(apiURL,data=jsonConvert)
        messages.success(request, 'your message has been sent!')
    inhouseInvs=inhouseInventory.objects.all()
    return render(request,"inventory/inHouseInv.html",{'inhouseInvs':inhouseInvs})

# Create your views here.
def invUpdate(request,sno):
    if request.method=='POST':
        productSno=request.POST.get('productSno')
        level=request.POST.get('level')
        qpp=request.POST.get('qpp')
        dimension=request.POST.get('dimension') 
        drawingno=request.POST.get('drawingno')
        availableNos=request.POST.get('availableNos')
        description=request.POST.get('description')
        timein=request.POST.get('timein')

        inhouseInv = inhouseInventory.objects.get(sno=sno)
        inhouseInv.productSno = productSno
        inhouseInv.level = level
        inhouseInv.qpp= qpp
        inhouseInv.dimension =dimension
        inhouseInv.drawingno =drawingno
        inhouseInv.availableNos =availableNos
        inhouseInv.description =description
        inhouseInv.timein =timein
        inhouseInv.save()
            # db.session.add(todo)
            # db.session.commit()
        return redirect("/invUpdate")
    inhouseInv=inhouseInventory.objects.get(sno=sno)
    return render(request, "inventory/invupdate.html",{'inhouseInv':inhouseInv})

def delete(request,sno):
    inhouseInv = inhouseInventory.objects.get(sno=sno)
    inhouseInv.delete()
    return redirect("/inv")

def updatedView(request,sno):
    inhouseInv = inhouseInventory.objects.get(sno=sno)
    return render(request,"update.html",{'inhouseInv':inhouseInv})

