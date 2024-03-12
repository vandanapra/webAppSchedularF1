from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from operations.models import Operation

# Create your models here.
class Product(models.Model):
    assembly_code = models.CharField(_("assembly_code"), max_length=50,null=True,blank=True)
    item = models.CharField(_("item_description"), max_length=500,null=True, blank=True)
    drg_no = models.CharField(_("drawing_no"), max_length=500,unique=True,null=True, blank=True)
    quantity = models.IntegerField(_("quantity"),default=1)
    parent_id = models.ForeignKey('self', related_name='parent', on_delete=models.CASCADE,null=True, blank=True)
    created_at = models.DateTimeField(_("created_at"), auto_now=True, auto_now_add=False)


    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return f"code: {self.assembly_code}, product: {self.item}, drg_no: {self.drg_no}"

    def get_absolute_url(self):
        return reverse("Product_detail", kwargs={"pk": self.pk})
    
    def product_parent(self):
        return self.parent_id

class ProductParentChildRelation(models.Model):
    item = models.ForeignKey(Product, related_name="parent_item", on_delete=models.CASCADE)
    child_item = models.ForeignKey(Product, related_name="child_item", on_delete=models.CASCADE)
    level = models.IntegerField(_("level"), default=0)
    created_at = models.DateTimeField(_("created_at"), auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = _("ProductParentChildRelation")
        verbose_name_plural = _("ProductParentChildRelations")

    def __str__(self):
        return f"item: {self.item}, child: {self.child_item}"

    def get_absolute_url(self):
        return reverse("ProductParentChildRelation_detail", kwargs={"pk": self.pk})

class OperationProduct(models.Model):
    operation = models.ForeignKey(Operation, related_name="operation_id", on_delete=models.CASCADE)
    input_items = models.ManyToManyField(Product, related_name="input_items")
    output_items = models.ManyToManyField(Product, related_name="output_items")
    created_at = models.DateTimeField(_("created_at"), auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = _("OperationProduct")
        verbose_name_plural = _("OperationProducts")

    def __str__(self):
        return self.operation.name

    def get_absolute_url(self):
        return reverse("OperationProduct_detail", kwargs={"pk": self.pk})




