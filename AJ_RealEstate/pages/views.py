from django.shortcuts import render
from listings.models import Listing


# Create your views here.

def index(request):
    latest = Listing.objects.order_by('-list_date')[:3]

    context = {
        'latest': latest
    }
    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')
