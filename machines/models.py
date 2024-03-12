from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from datetime import datetime


# Create your models here.
class Machine(models.Model):
    STATUS = (('running-100ef','Productive'),('running-below-100ef','Productive (<100%)'),('connected-and-ready','Connected and Ready'),('disconnected','Disconnected'),('machine-not-in-use','Machine Not In Use'),('alarm','Alarm'),('not-ready-for-operation','Not Ready For Operation'),('breakdown','Breakdown'))
    name = models.CharField(_("Name"), max_length=50)
    line = models.CharField(_("Line"), max_length=50)
    manufacturer = models.CharField(_("manufacturer"), max_length=500,null=True, blank=True)
    shop_name = models.CharField(_("shop_name"), max_length=500,null=True, blank=True)
    machine_no = models.CharField(_("Machine No"), max_length=50)
    status = models.CharField(_("Status"),choices=STATUS,max_length=50,default='running-100ef')
    operation = models.CharField(_("Operation"), max_length=500)
    created_at = models.DateTimeField(_("created_at"), auto_now=True, auto_now_add=False)
    modified_at = models.DateTimeField(_("modified_at"), auto_now=False, auto_now_add=True)
    class Meta:
        verbose_name = _("Machine")
        verbose_name_plural = _("Machines")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Machine_detail", kwargs={"pk": self.pk})
