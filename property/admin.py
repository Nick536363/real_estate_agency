from django.contrib import admin
from .models import Flat


class Admin(admin.ModelAdmin):
    search_fields = ("address", "town", "owner")
    readonly_fields = ["created_at"]


admin.site.register(Flat, Admin)
