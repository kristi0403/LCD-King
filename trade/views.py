from django.shortcuts import render

# Create your views here.


def trade(request):
    """ A view to return the trade details """

    return render(request, 'trade/trade.html')
