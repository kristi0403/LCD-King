from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_categories_details, name='service_categories')
]
