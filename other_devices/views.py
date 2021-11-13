from django.shortcuts import render

# Create your views here.


def other_devices(request):
    """ A view to return other device enquires """

    return render(request, 'other_devices/other_devices.html')
