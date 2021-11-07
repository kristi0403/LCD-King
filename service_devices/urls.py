from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_service_devices, name='service_devices'),
    path('<service_device_id>', views.service_device_detail, name='service_device_detail'),
]
