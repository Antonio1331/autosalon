from django.contrib import admin

from .models import Brand, Car

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "country")
    search_fields = ("name", "country")

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "brand", "year", "price")
    list_filter = ("brand", "year")
    search_fields = ("name",)

