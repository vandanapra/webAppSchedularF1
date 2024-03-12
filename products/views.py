from django.shortcuts import render
from django.views.generic import ListView
from django_tables2 import tables,SingleTableView
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django_filters import FilterSet
from django_tables2.export.views import ExportMixin

from .models import *

# Create your views here.
class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {"item":["contains"]}
    


class ProductTable(tables.Table):
    class Meta:
        model = Product
        template_name = "django_tables2/bootstrap5-responsive.html"
        fields = ('assembly_code','item','drg_no','created_at')

class ProductListView(ExportMixin,SingleTableMixin, FilterView):

    model = Product
    table_class = ProductTable
    template_name = "comp_details.html"
    filterset_class = ProductFilter
    export_formats = ('csv','json','xlsx')
    paginate_by = 10

