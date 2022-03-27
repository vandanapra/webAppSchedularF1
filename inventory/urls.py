from django.contrib import admin
from django.urls import path
from inventory import views
urlpatterns = [
    path('',views.inventory,name='inv'),
    path('invUpdate/<int:sno>',views.invUpdate, name='update'),
    path('delete/<int:sno>',views.delete, name='delete'),
    path('<int:sno>',views.updatedView,name='updated_view'),

]