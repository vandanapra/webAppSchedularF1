from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('assembly_code','item','drg_no','product_parent','quantity','created_at')
    search_fields = ('drg_no','assembly_code','item')
    raw_id_fields = ('parent_id',)

@admin.register(ProductParentChildRelation)
class ProductParentChildRelationAdmin(admin.ModelAdmin):
    list_display = ('item','child_item','level')
    search_fields = ('item','child_item','level')
    

@admin.register(OperationProduct)
class OperationProductAdmin(admin.ModelAdmin):
    list_display = ('operation','created_at')
    

    

    

