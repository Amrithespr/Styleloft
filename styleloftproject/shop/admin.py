from django.contrib import admin

from styleapp.models import FemaleServices, MaleServices
from .models import Category, Product


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available', 'category', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20


admin.site.register(Product, ProductAdmin)


admin.site.register(FemaleServices)
admin.site.register(MaleServices)
