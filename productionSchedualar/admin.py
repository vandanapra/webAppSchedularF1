from django.contrib import admin
from productionSchedualar.models import productionOrder,machineDetails,componentDetails

# Register your models here.
admin.site.register(productionOrder)
admin.site.register(machineDetails)
admin.site.register(componentDetails)
