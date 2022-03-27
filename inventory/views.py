from django.shortcuts import render,redirect
from datetime import datetime
from inventory.models import inhouseInventory
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def inventory(request):
    # python_list  = []
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
        # python_list.append(detail)
        # print(python_list)
        messages.success(request, 'your message has been sent!')
    inhouseInvs=inhouseInventory.objects.all()
    return render(request,"inHouseInv.html",{'inhouseInvs':inhouseInvs})
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
    return render(request, "invupdate.html",{'inhouseInv':inhouseInv})



def delete(request,sno):
    inhouseInv = inhouseInventory.objects.get(sno=sno)
    inhouseInv.delete()
    return redirect("/inv")

def updatedView(request,sno):
    inhouseInv = inhouseInventory.objects.get(sno=sno)
    return render(request,"update.html",{'inhouseInv':inhouseInv})

