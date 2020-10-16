from django.shortcuts import render


# Create your views here.

def listings_index(request):
    return render(request, 'listings/listings_index.html')


def listing(request):
    return render(request, 'listings/listing.html')
