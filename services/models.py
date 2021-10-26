from django.db import models


class Category_of_service(models.Model):

    class Meta:
        verbose_name_plural = 'Categories_of_services'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Device_of_service(models.Model):

    class Meta:
        verbose_name_plural = 'Devices_of_services'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Service(models.Model):

    device_of_service = models.ForeignKey('Device_of_service', null=True, blank=True,
                               on_delete=models.SET_NULL)
    category_of_service = models.ForeignKey('Category_of_service', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
