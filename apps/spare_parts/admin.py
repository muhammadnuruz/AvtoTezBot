from django.contrib import admin

from apps.spare_parts.models import SpareParts


class SparePartsAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    ordering = ('created_at',)


admin.site.register(SpareParts, SparePartsAdmin)
