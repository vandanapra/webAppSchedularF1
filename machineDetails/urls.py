from django.contrib import admin
from django.urls import path
from inventory import views
urlpatterns = [
    path('machineDetails',views.machineDetails,name='machineDetails')
    ]