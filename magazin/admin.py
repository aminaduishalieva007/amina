from django.contrib import admin
from magazin.models import Shop

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
