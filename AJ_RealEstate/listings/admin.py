from django.contrib import admin
from .models import Listing


# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    class Meta:
        model = Listing

    list_display = ['id', 'title', 'address', 'city', 'price', 'price', 'photo_main', 'realtor', 'is_published']
    list_display_links = ['id', 'title']
    list_filter = ['realtor']
    list_editable = ('is_published',)
    list_per_page = 10


admin.site.register(Listing, ListingAdmin)
