from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from products.models import Product
# Create your models here.

class Location(models.Model):
    location = models.CharField(_("Location"), max_length=50)

    class Meta:
        verbose_name = _("Location")
        verbose_name_plural = _("Locations")

    def __str__(self):
        return self.location

    def get_absolute_url(self):
        return reverse("Location_detail", kwargs={"pk": self.pk})


class Inventory(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    location = models.ForeignKey("Location", verbose_name=_("Location"), on_delete=models.CASCADE,null=True, blank=True)
    roq_minimum_quantity = models.CharField(_("ROQ Min Quantity"), max_length=50,null=True, blank=True)
    roq_maximum_quantity = models.CharField(_("ROQ Max Quantity"), max_length=50,null=True, blank=True)
    roq_minimum_period_of_cover = models.CharField(_("ROQ Min Period of Cover"), max_length=50,null=True, blank=True)
    roq_maximum_period_of_cover = models.CharField(_("ROQ Max Period of Cover"), max_length=50,null=True, blank=True)
    safety_stock_minimum_quantity = models.CharField(_("Safety Stock Min Quantity"), max_length=50,null=True, blank=True)
    safety_stock_maximum_quantity = models.CharField(_("Safety Stock Max Quantity"), max_length=50,null=True, blank=True)
    safety_stock_minimum_period_of_cover = models.CharField(_("Safety Stock Min Period of Cover"), max_length=50,null=True, blank=True)
    safety_stock_maximum_period_of_cover = models.CharField(_("Safety Stock Min Period of Cover"), max_length=50,null=True, blank=True)
    service_level = models.CharField(_("Service Level"), max_length=50,null=True, blank=True)
    lead_time = models.CharField(_("Lead Time"), max_length=50,null=True, blank=True)
    lead_time_deviation = models.CharField(_("Lead Time Deviation"), max_length=50,null=True, blank=True)
    donot_stock = models.BooleanField(default=False)
    current_available = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    def products(self):
        return self.product.item
    

    class Meta:
        verbose_name = _("Inventory")
        verbose_name_plural = _("Inventory")
