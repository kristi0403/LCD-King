from django.contrib import admin
from .models import Service_device, Device_category, Service

# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
        'service_device',
        'price',
    )

class Service_deviceAdmin(admin.ModelAdmin):
    list_display = (
        'device_category',
        'name',
        'friendly_name',
        'image',
    )


class Device_categoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )


admin.site.register(Service_device, Service_deviceAdmin)
admin.site.register(Device_category, Device_categoryAdmin)
admin.site.register(Service, ServiceAdmin)
