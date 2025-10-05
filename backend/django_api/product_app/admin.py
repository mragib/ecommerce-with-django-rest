from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import Product, Category, Brand, ProductLine, ProductImage


class EditLinkInline(object):
    def edit(self, instance):
        if not instance.pk:  # only saved objects get an edit link
            return ""
        url = reverse(
            f"admin:{instance._meta.app_label}_{instance._meta.model_name}_change",
            args=[instance.pk],
        )
        return mark_safe(f'<a href="{url}">Edit</a>')


class ProductLineImagesInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductLineAdmin(admin.ModelAdmin):
    #inlines = [ProductLineImagesInline]
    pass


class ProductLineInline(EditLinkInline, admin.TabularInline):
    model = ProductLine
    extra = 1
    readonly_fields = ("edit",)


# @admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    search_fields = ("name",)
    list_filter = ("category", "brand")
    inlines = [ProductLineInline]


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductLine, ProductLineAdmin)
admin.site.register(Category)
admin.site.register(Brand)
