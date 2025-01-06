from django.contrib import admin
from apps.contacts.models import Contacts


class BrandsInline(admin.TabularInline):
    model = Contacts.brands.through
    extra = 0
    verbose_name = "Brand"
    verbose_name_plural = "Brands"


class SparePartsInline(admin.TabularInline):
    model = Contacts.spare_parts.through
    extra = 0
    verbose_name = "Spare Part"
    verbose_name_plural = "Spare Parts"


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number', 'number_of_brands', 'number_of_spare_parts', 'created_at')
    list_editable = ('address', 'phone_number')
    list_filter = ('brands', 'spare_parts', 'created_at')
    search_fields = ('name', 'address', 'phone_number', 'brands__name', 'spare_parts__name')
    list_per_page = 20
    filter_horizontal = ('brands', 'spare_parts')
    inlines = [BrandsInline, SparePartsInline]
    readonly_fields = ('created_at', 'updated_at')
    save_on_top = True
    fieldsets = (
        ("Basic information", {
            'fields': ('name', 'address', 'landmark', 'phone_number', 'created_at')
        }),
    )

    @admin.display(description="Number of Brands")
    def number_of_brands(self, obj):
        return obj.brands.count()

    @admin.display(description="Number of Spare Parts")
    def number_of_spare_parts(self, obj):
        return obj.spare_parts.count()

    actions = ['export_to_csv']

    def export_to_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="contacts.csv"'

        writer = csv.writer(response)
        writer.writerow(['Name', 'Address', 'Phone Number', 'Number of Brands', 'Number of Spare Parts', 'Created At'])

        for contact in queryset:
            writer.writerow([
                contact.name,
                contact.address,
                contact.phone_number,
                contact.brands.count(),
                contact.spare_parts.count(),
                contact.created_at,
            ])

        self.message_user(request, f"{queryset.count()} contacts exported to CSV file.")
        return response

    export_to_csv.short_description = "Export selected contacts in CSV format"
