from django.db import models


class SpareParts(models.Model):
    name = models.CharField("Название (на узбекском)", max_length=100)
    ru_name = models.CharField("Название (на русском)", max_length=100)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    class Meta:
        verbose_name = "Запасная часть"
        verbose_name_plural = "Запасные части"

    def __str__(self):
        return self.ru_name
