from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_service_devices, name='service_devices'),
]
