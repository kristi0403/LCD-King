from django.contrib import admin
from .models import Product, Category, Device, Special_category, Sub_category, Service

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Device)
admin.site.register(Special_category)
admin.site.register(Sub_category)
admin.site.register(Service)
