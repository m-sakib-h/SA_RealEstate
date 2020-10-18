from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import Listing

# Create your views here.

def listings_index(request):
    listing_list = Listing.objects.all()  # [:1]    # Suppose 6 listing

    paginator = Paginator(listing_list, 3)
    page = request.GET.get('page', 1)

    try:
        paginator_listing_ = paginator.page(page)
    except PageNotAnInteger:
        paginator_listing_ = paginator.page(1)      # By_Default kon page show korba
    except EmptyPage:
        paginator_listing_ = paginator.num_pages

    context = {
        'listing_list': paginator_listing_
    }
    return render(request, 'listings/listings_index.html', context)


def listing(request, listing_id):
    listing_id = Listing.objects.get(id=listing_id)
    seller_of_the_month = Listing.objects.filter()
    context = {
        'listing_id': listing_id
    }

    return render(request, 'listings/listing.html', context)
