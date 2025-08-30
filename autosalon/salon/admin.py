from django.contrib import admin
from django.utils.html import format_html
from .models import Brand, Car, Comment


def image_preview(obj):
    if obj.image:
        return format_html('<img src="{}" width="100" />', obj.image.url)
    return "Rasm yo‘q"
image_preview.short_description = "Rasm"


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "country")
    search_fields = ("name", "country")
    list_filter = ("country",)
    ordering = ("name",)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "brand", "year", "price", "is_available", image_preview)
    list_editable = ("price", "is_available")
    list_filter = ("brand", "year", "is_available")
    search_fields = ("name", "brand__name")
    list_display_links = ("name",)
    inlines = [CommentInline]
    fields = ("brand", "name", "year", "price", "image", "is_available")
