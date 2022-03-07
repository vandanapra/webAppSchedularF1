from django.contrib import admin
from django.urls import path
from productionSchedualar import views
from django.views.generic import TemplateView

urlpatterns = [
    path('',views.index, name='productionSchedualar'),
    path('operations_chart',views.operationsChart, name='operations_chart'),
    path('machine_loading',views.machineLoading, name='machine_loading'),
    path('place_order',views.placeOrder, name='place_order'),
    path('generate_schedule',views.generateSchedule, name='generate_schedule'),
    path('update/<int:sno>',views.update, name='update'),
    path('delete/<int:sno>',views.delete, name='delete'),
    path('<id>',views.updatedView,name='updated_view'),

]