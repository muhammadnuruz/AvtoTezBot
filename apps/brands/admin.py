from django.contrib import admin

from apps.brands.models import Brands

class BrandsAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_at')
    ordering = ('category', 'created_at')


admin.site.register(Brands, BrandsAdmin)
