from django.contrib import admin
from .models import Flat, Complaint, Owner


class Admin(admin.ModelAdmin):
    search_fields = ("address", "town", "owner")
    readonly_fields = ["created_at"]
    list_display = ["address", "price", "new_building", "construction_year", "town"]
    list_editable = ["new_building"]
    list_filter = ["new_building"]
    raw_id_fields = ["liked_by"]

admin.site.register(Flat, Admin)
admin.site.register(Complaint)
admin.site.register(Owner)