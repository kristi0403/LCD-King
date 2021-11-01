from django.contrib import admin
from .models import Service_category

# Register your models here.


class Service_categoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
        'price',
    )


admin.site.register(Service_category, Service_categoryAdmin)
