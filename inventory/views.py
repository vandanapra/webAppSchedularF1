from django.shortcuts import render
from django.views.generic import ListView
from django_tables2 import tables,SingleTableView
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django_filters import FilterSet,rest_framework
from django_tables2.export.views import ExportMixin
from rest_framework import generics, status, authentication, permissions
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from .serializers import *


from .models import *

# Create your views here.
# class InventoryFilter(FilterSet):
#     class Meta:
#         model = Inventory
#         fields = {"product":["product__item_contains"]}
    


class InventoryTable(tables.Table):
    class Meta:
        model = Inventory
        template_name = "django_tables2/bootstrap5-responsive.html"
        fields = ('product','location','roq_minimum_quantity','roq_maximum_quantity','roq_minimum_period_of_cover','roq_maximum_period_of_cover','safety_stock_minimum_quantity','safety_stock_maximum_quantity','safety_stock_minimum_period_of_cover','safety_stock_maximum_period_of_cover','service_level','lead_time','lead_time_deviation','donot_stock','current_available','created_at','updated_at')

class InventoryListView(ExportMixin,SingleTableMixin, FilterView):

    model = Inventory
    table_class = InventoryTable
    template_name = "inventory/inHouseInventory.html"
    # filterset_class = InventoryFilter
    export_formats = ('csv','json','xlsx')
    paginate_by = 10


class InventoryAPI(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,SessionAuthentication)
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['product__item','location__location']

class InventoryUpdateAPI(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,SessionAuthentication)
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['product__item','location__location']
