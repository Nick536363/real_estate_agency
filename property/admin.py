from django.contrib import admin
from .models import Flat, Complaint, Owner


class FlatOptions(admin.ModelAdmin):
    search_fields = ("address", "town", "owner")
    readonly_fields = ["created_at"]
    list_display = ["address", "price", "new_building", "construction_year", "town"]
    list_editable = ["new_building"]
    list_filter = ["new_building"]
    raw_id_fields = ["liked_by"]


class OwnerOptions(admin.ModelAdmin):
    raw_id_fields = ["owned_flats"]


admin.site.register(Flat, FlatOptions)
admin.site.register(Complaint)
admin.site.register(Owner, OwnerOptions)