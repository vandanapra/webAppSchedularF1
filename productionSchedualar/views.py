from django.shortcuts import render,HttpResponse,redirect
from datetime import date, datetime
from productionSchedualar.models import machineDetails, productionOrder,componentDetails
from django.contrib import messages
from src import main
from django.views.decorators.csrf import csrf_protect


# Create your views here.
@csrf_protect
def index (request):
    context = {
        "variable":"vandana is great girl" }
    # messages.success(request,"this is a text message")
    return render(request, "index.html",context)

def operationsChart (request):
    return render(request, "operations_chart.html")

def machineLoading (request):
    return render(request, "machine_loading.html")
    
def placeOrder (request):
    if request.method =="POST":
        OR_no=request.POST.get('OR_no')
        variant=request.POST.get('variant')
        start_date=request.POST.get('start_date')
        end_date=request.POST.get('end_date') 
        quantity=request.POST.get('quantity') 
        priority=request.POST.get('priority') 
        order=productionOrder(orderRefNo=OR_no,orderVariant=variant,orderStartDate=start_date,orderEndDate=end_date,orderQuantity=quantity,orderPriority=priority,currentDate=datetime.today())
        order.save()
        messages.success(request, 'your Order has been sent!')
    orders = productionOrder.objects.all()
    return render(request, "place_order.html",{'orders':orders})

def generateSchedule (request):
    todaysOrder = productionOrder.objects.filter(currentDate = datetime.today()).order_by("sno")
    main.main(request,todaysOrder)
    return render(request, "machine_loading.html")
    
# @app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(request,sno):
    if request.method=='POST':
        OR_no=request.POST.get('OR_no')
        variant=request.POST.get('variant')
        start_date=request.POST.get('start_date')
        end_date=request.POST.get('end_date') 
        quantity=request.POST.get('quantity') 
        priority=request.POST.get('priority')
        order = productionOrder.objects.get(sno=sno)
        order.orderRefNo = OR_no
        order.orderVariant = variant
        order.orderStartDate = start_date
        order.orderEndDate =end_date
        order.ordeQuantity =quantity
        order.orderPriority =priority
        order.save()
            # db.session.add(todo)
            # db.session.commit()
        return redirect("/place_order")
        
    order = productionOrder.objects.get(sno=sno)
    return render(request, "update.html",{'order':order})



def delete(request,sno):
    order = productionOrder.objects.get(sno=sno)
    order.delete()
    return redirect("/place_order")

def updatedView(request,sno):
    order = productionOrder.objects.get(sno=sno)
    return render(request,"update.html",{'order':order})

def mcDetails(request):
    if request.method =="POST":
        machine_name=request.POST.get('machine_name')
        Manufacturer=request.POST.get('Manufacturer')
        shopName=request.POST.get('shopName')
        MachineNo=request.POST.get('MachineNo') 
        description=request.POST.get('description') 
        remarks=request.POST.get('remarks') 
        mcDetails=machineDetails(machine_name=machine_name,Manufacturer=Manufacturer,shopName=shopName,MachineNo=MachineNo,Description=description,remarks=remarks,currentDate=datetime.today())
        mcDetails.save()
        messages.success(request, 'your Order has been sent!')
    details = machineDetails.objects.all()
    return render(request, "mc_details.html",{'detail':details})
   

def compDetails(request):
    if request.method =="POST":
        component_name=request.POST.get('component_name')
        DrawingNo=request.POST.get('DrawingNo')
        qpp=request.POST.get('qpp')
        Level=request.POST.get('Level') 
        description=request.POST.get('description') 
        modelName=request.POST.get('modelName') 
        cpDetails=componentDetails(component_name=component_name,DrawingNo=DrawingNo,qpp=qpp,Level=Level,description=description,modelName=modelName,currentDate=datetime.today())
        cpDetails.save()
        messages.success(request, 'your Order has been sent!')
    component_details = componentDetails.objects.all()
    return render(request,"comp_details.html",{'cpdetail':component_details})

def operationDetails(request):
    return render(request,"operation_details.html")
