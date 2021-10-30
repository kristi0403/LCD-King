from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models.functions import Lower
from django.db.models import Q
from .models import Service, Category_of_service, Device_of_service

# Create your views here.


def all_services(request):
    """ A view to show all services, including sorting and searching """

    services = Service.objects.all()

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                services = services.annotate(lower_name=Lower('name'))
            if sortkey == 'category_of_service':
                sortkey = 'category_of_service__name'
        if 'direction' in request.GET:
            direction = request.GET['direction']
            if direction == 'desc':
                sortkey = f'-{sortkey}'
        services = services.order_by(sortkey)

        if 'device_of_service' in request.GET:
            devices_of_services = request.GET['device_of_service'].split(',')
            services = services.filter(
                device_of_service__name__in=devices_of_services)
            devices_of_services = Device_of_service.objects.filter(
                name__in=devices_of_services)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('categories_of_services'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            services = services.filter(queries)
    
    query = None
    categories_of_services = None
    sort = None
    direction = None
    current_sorting = f'{sort}_{direction}'

    context = {
        'services': services,
        'search_term': query,
        'current_categories': categories_of_services,
        'current_sorting': current_sorting,
    }

    return render(request, 'services/services.html', context)


def all_categories_of_services(request):
    """ A view to show all categories of services, including sorting and searching """

    categories_of_services = Category_of_service.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('categories_of_services'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            categories_of_services = categories_of_services.filter(queries)

    context = {
        'categories_of_services': categories_of_services,
        'search_term': query,
    }

    return render(request, 'services/categories_of_services.html', context)


def all_devices_of_services(request):
    """ A view to show all devices of services, including sorting and searching """

    devices_of_services = Device_of_service.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('devices_of_services'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            devices_of_services = devices_of_services.filter(queries)

    context = {
        'devices_of_services': devices_of_services,
        'search_term': query,
    }

    return render(request, 'services/devices_of_services.html', context)