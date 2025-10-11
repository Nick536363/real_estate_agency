from django.contrib import admin
from .models import Flat


class Admin(admin.ModelAdmin):
    search_fields = ("address", "town", "owner")
    readonly_fields = ["created_at"]
    list_display = ["address", "price", "new_building", "construction_year", "town"]
    list_editable = ["new_building"]
    list_filter = ["new_building"]


admin.site.register(Flat, Admin)
