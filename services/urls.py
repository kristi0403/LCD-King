from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_categories_of_services, name='categories_of_services'),
    path('', views.all_devices_of_services, name='devices_of_services'),
    path('', views.all_services, name='services'),
]
