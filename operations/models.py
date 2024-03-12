from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from machines.models import Machine

# Create your models here.
class Operation(models.Model):
    name = models.CharField(_("operation"), max_length=500)
    machine = models.ManyToManyField(Machine, related_name='machine_id')
    time = models.CharField(_("Time Taken (in minutes)"), max_length=50)
    
    class Meta:
        verbose_name = _("Operation")
        verbose_name_plural = _("Operations")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Operation_detail", kwargs={"pk": self.pk})

