from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    filter_horizontal = ('machine',)
    
    
