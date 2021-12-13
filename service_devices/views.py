from django.shortcuts import render, redirect, reverse, get_object_or_404, get_list_or_404
from django.contrib import messages
from django.db.models.functions import Lower
from django.db.models import Q
from .models import Service_device, Device_category, Service

# Create your views here.


def all_service_devices(request):
    """ A view to show all the devices of each category """

    service_devices = Service_device.objects.all()
    sort = None
    direction = None
    query = None
    device_categories = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                service_devices = service_devices.annotate(lower_name=Lower('name'))
            if sortkey == 'service_device':
                sortkey = 'service_device__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            service_devices = service_devices.order_by(sortkey)

        if 'device_category' in request.GET:
                device_categories = request.GET['device_category'].split(',')
                service_devices = service_devices.filter(device_category__name__in=device_categories)
                device_categories = Device_category.objects.filter(
                    name__in=device_categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('service_devices'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            service_devices = service_devices.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'service_devices': service_devices,
        'search_term': query,
        'current_categories': device_categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'service_devices/service_devices.html', context)


def service_device_detail(request, service_device_id):
    """ A view to show individual service_device details """

    service_device = get_object_or_404(Service_device, pk=service_device_id)
    services = get_list_or_404(Service, service_device=service_device_id)
    context = {
        'service_device': service_device,
        'services': services,
    }

    return render(request, 'service_devices/service_device_detail.html', context)
