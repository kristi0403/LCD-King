from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models.functions import Lower
from django.db.models import Q
from .models import Service, Category_of_service, Device_of_service

# Create your views here.


def all_services(request):
    """ A view to show all services, including sorting and searching """

    services = Service.objects.all()
    query = None
    categories_of_services = None
    sort = None
    direction = None

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

        if 'category_of_service' in request.GET:
            categories_of_services = request.GET['category_of_service'].split(',')
            services = services.filter(category_of_service__name__in=categories_of_services)
            categories_of_services = Category_of_service.objects.filter(name__in=categories_of_services)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('services'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            services = services.filter(queries)

        if 'device_of_service' in request.GET:
            devices_of_services = request.GET['device_of_service'].split(',')
            services = services.filter(device_of_service__name__in=devices_of_services)
            devices_of_services = Device_of_service.objects.filter(
                name__in=devices_of_services)

    current_sorting = f'{sort}_{direction}'

    context = {
        'services': services,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'services/services.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)

