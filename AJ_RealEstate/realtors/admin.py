from django.contrib import admin
from .models import Realtor

# Register your models here.

class RealtorAdmin(admin.ModelAdmin):
    class Meta:
        model = Realtor

    list_display = ['id', 'name', 'photo', 'email', 'phone', 'is_mvp']
    list_display_links = ['id']
    list_editable = ('is_mvp',)
    list_filter = ('name',)
    search_fields = ('name', 'email', 'phone', 'message',)
    list_per_page = 15


admin.site.register(Realtor, RealtorAdmin)
