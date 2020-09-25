from django.contrib import admin

from .models import Flat
from property.models import Flat
 
 
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner',]
    readonly_fields = ['created_at',]
    list_display  = ['town', 'new_building', "address", "price"]
    list_editable = ['new_building',]
admin.site.register(Flat, FlatAdmin)