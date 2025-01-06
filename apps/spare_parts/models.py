from django.db import models


class SpareParts(models.Model):
    name = models.CharField(max_length=100)
    ru_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Spare part"
        verbose_name_plural = "Spare parts"

    def __str__(self):
        return self.name
