from django.contrib import admin
from .models import (Product, Category, Media, Brand, 
Colour, WeightUnit, ProductType, SubProduct, 
Stock, Size
)
# Register your models here.

class SizeAdmin(admin.ModelAdmin):
    ordering = ['size']
    list_display = ['size', 'slug']
    list_display_links = ['size']
    list_per_page = 50


class CategoryAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ['is_active', 'name', 'slug']
    list_display_links = ['slug']
    list_per_page = 50


class CategoryAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = [ 'name', 'slug']
    list_display_links = ['slug']
    list_per_page = 50

class ProductAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = [ 'name', 'slug']
    list_display_links = ['slug']
    list_per_page = 50

class SubProductAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ['name', 'sale_price', 'in_stock', 'product', 'slug']
    list_display_links = ['slug']
    list_per_page = 50



admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Media)
admin.site.register(ProductType)
admin.site.register(Brand)
admin.site.register(Colour)
admin.site.register(SubProduct, SubProductAdmin)
admin.site.register(Stock)
admin.site.register(Size, SizeAdmin)