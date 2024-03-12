from unicodedata import name
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('machine-csv',write_to_model),
    path('operation-excel',write_to_model_operation),
    path('products-list',write_to_model_products)
    ]