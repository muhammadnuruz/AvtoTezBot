from django.db import models

from apps.brands.models import Brands
from apps.spare_parts.models import SpareParts


class Contacts(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=100)
    brands = models.ManyToManyField(Brands, related_name="contacts")
    spare_parts = models.ManyToManyField(SpareParts, related_name="contacts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.name
