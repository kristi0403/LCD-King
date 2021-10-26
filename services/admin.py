from django.contrib import admin
from .models import Service, Category_of_service, Device_of_service

# Register your models here.


class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category_of_service',
        'price',
        'device_of_service',
    )

    ordering = ('name',)


class Category_of_serviceAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class Device_of_serviceAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Service, ServiceAdmin)
admin.site.register(Category_of_service, Category_of_serviceAdmin)
admin.site.register(Device_of_service, Device_of_serviceAdmin)
