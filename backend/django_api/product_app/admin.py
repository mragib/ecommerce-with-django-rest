from django.contrib import admin
from .models import Product, Category, Brand, ProductLine


class ProductLineInline(admin.TabularInline):
    model = ProductLine
    extra = 1


# @admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    search_fields = ("name",)
    list_filter = ("category", "brand")
    inlines = [ProductLineInline]


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Brand)
