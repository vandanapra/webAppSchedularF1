from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class productionOrder(models.Model):
    orderId = models.AutoField(_("order_id"),primary_key=True)
    orderRefNo = models.CharField(max_length=122,null=True, blank=True)
    orderVariant = models.CharField(max_length=122,null=True, blank=True)
    orderStartDate = models.DateField(null=True)
    orderEndDate = models.DateField(null=True)
    orderQuantity = models.CharField(max_length=122,null=True, blank=True)
    orderPriority = models.CharField(max_length=122,null=True, blank=True)
    status = models.CharField(_("status"), max_length=50,choices=(('pending', 'pending'),('complete', 'complete')))
    created_at = models.DateField(_("created_at"), auto_now=True, auto_now_add=False)
    modified_at = models.DateField(_("modified_at"),auto_now=False, auto_now_add=True)

    class Meta:
        db_table = 'tb_production_orders'
        verbose_name = _("Sales Order")
        verbose_name_plural = _("Sales Orders")
