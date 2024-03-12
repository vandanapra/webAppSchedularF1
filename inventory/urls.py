from django.contrib import admin
from django.urls import path
from inventory import views

urlpatterns = [
    path('planning/',views.InventoryListView.as_view(),name="inventory-view"),
    path('api/planning/',views.InventoryAPI.as_view()),
    path('api/planning/update/<int:pk>',views.InventoryUpdateAPI.as_view()),
]