from django.contrib import admin

from .models import Flat
from property.models import Flat, Appeal, Owner
 
 
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner',]
    readonly_fields = ['created_at',]
    list_display  = ["address", 'price', 'new_building', "construction_year", 'town',]
    list_editable = ['new_building',]
    list_filter = ['new_building', 'rooms_number', 'has_balcony',]
    raw_id_fields = ["who_liked"]

class AppealAdmin(admin.ModelAdmin):
    raw_id_fields = ("apartment", 'author')
    list_display = ["author", "apartment"]
    

class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ["owned_apartments",]
    list_display = ["owner", "owner_pure_phone"]



admin.site.register(Flat, FlatAdmin)
admin.site.register(Appeal, AppealAdmin)
admin.site.register(Owner, OwnerAdmin)