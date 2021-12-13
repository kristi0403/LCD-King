from django.db import models


class Device_category(models.Model):

    class Meta:
        verbose_name_plural = 'Device_categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)


    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Service(models.Model):

    class Meta:
        verbose_name_plural = 'Services'

    service_device = models.ForeignKey('Service_device', null=True, blank=True,
                                        on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)


    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Service_device(models.Model):

    device_category = models.ForeignKey('Device_category', null=True, blank=True,
                                        on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
