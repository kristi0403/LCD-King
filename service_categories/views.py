from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models.functions import Lower
from django.db.models import Q
from .models import Service_category

# Create your views here.


def service_categories_details(request):
    """ A view to return the service_categories """

    service_categories = Service_category.objects.all()

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                service_categories = service_categories.annotate(lower_name=Lower('name'))
            if sortkey == 'service_categories':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            service_categories = service_categories.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('service_categories'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            service_categories = service_categories.filter(queries)

    query = None

    context = {
        'service_categories': service_categories,
        'search_term': query,
    }

    return render(request, 'service_categories/service_categories.html', context)
