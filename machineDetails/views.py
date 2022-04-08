from django.shortcuts import render

# Create your views here.
def machineDetails(request):
    return render(request,"mc_details.html")