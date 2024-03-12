from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ('name','line','machine_no','status','operation','created_at','modified_at')
    

