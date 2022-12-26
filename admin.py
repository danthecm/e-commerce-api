from django.contrib import admin
from .models import Size


class SizeAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'size', 'slug']
    list_display_links = ['size']
    list_per_page = 50


admin.site.register(Size, SizeAdmin)
