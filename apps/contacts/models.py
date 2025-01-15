from django.db import models

from apps.brands.models import Brands
from apps.spare_parts.models import SpareParts


class Contacts(models.Model):
    name = models.CharField("Имя", max_length=100)
    address = models.CharField("Адрес", max_length=100)
    landmark = models.CharField("Ориентир (на узбекском)", max_length=100, blank=True, null=True)
    landmark_ru = models.CharField("Ориентир (на русском)", max_length=100, blank=True, null=True)
    phone_number = models.CharField("Номер телефона", max_length=100)
    brands = models.ManyToManyField(Brands, verbose_name="Бренды", related_name="contacts")
    spare_parts = models.ManyToManyField(SpareParts, verbose_name="Запасные части", related_name="contacts")
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return self.name
