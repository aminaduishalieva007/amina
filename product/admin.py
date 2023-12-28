from django.contrib import admin
from product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_display_links = ('name', 'price')
