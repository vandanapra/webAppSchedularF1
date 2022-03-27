from django.contrib import admin
from django.urls import path
from HMI import views

urlpatterns = [
    path('',views.hmi,name='HMI'),
]