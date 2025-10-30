from django.contrib import admin
from .models import Flat, Complaint, Owner


class AdminInline(admin.TabularInline):
    model = Flat.owners.through
    raw_id_fields = ["owner", "flat"]


class FlatOptions(admin.ModelAdmin):
    search_fields = ("address", "town", "owner")
    readonly_fields = ["created_at"]
    list_display = ["address", "price", "new_building", "construction_year", "town"]
    list_editable = ["new_building"]
    list_filter = ["new_building"]
    raw_id_fields = ["liked_by"]
    inlines = [AdminInline]
    exclude = ["owners"]

class OwnerOptions(admin.ModelAdmin):
    raw_id_fields = ["flats"]    


admin.site.register(Flat, FlatOptions)
admin.site.register(Complaint)
admin.site.register(Owner, OwnerOptions)