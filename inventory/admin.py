from django.contrib import admin
from inventory.models import Inventory
# Register your models here.

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('products','location','current_available','donot_stock','created_at','updated_at')
    raw_id_fields = ('product',)

