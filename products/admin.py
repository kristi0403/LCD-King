from django.contrib import admin
from .models import Product, Category, Device, Special_category, Sub_category, Service

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'grade',
        'image',
        'device',
        'special_category',
        'sub_category',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class DeviceAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'price',
    )


class Special_categoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class Sub_categoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Special_category, Special_categoryAdmin)
admin.site.register(Sub_category, Sub_categoryAdmin)
admin.site.register(Service, ServiceAdmin)
