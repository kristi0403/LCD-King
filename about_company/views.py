from django.shortcuts import render

# Create your views here.


def company_details(request):
    """ A view to return the company details """

    return render(request, 'about_company/about_company.html')
