from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(productionOrder)
class productionOrderAdmin(admin.ModelAdmin):
    list_display = ('orderId','orderRefNo','orderVariant','orderStartDate','orderEndDate','orderQuantity','orderPriority','status','created_at','modified_at')
    

