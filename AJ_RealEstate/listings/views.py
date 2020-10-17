from django.shortcuts import render
from .models import Listing

# Create your views here.

def listings_index(request):
    listing_list = Listing.objects.all()

    context = {
        'listing_list': listing_list
    }
    return render(request, 'listings/listings_index.html', context)

def listing(request, listing_id):
    listing_id = Listing.objects.get(id=listing_id)
    seller_of_the_month = Listing.objects.filter()
    context = {
        'listing_id': listing_id
    }

    return render(request, 'listings/listing.html', context)
