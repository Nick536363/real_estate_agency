from django.contrib import admin
from .models import Flat


class Admin(admin.ModelAdmin):
    search_fields = ("address", "town", "owner")


admin.site.register(Flat, Admin)
