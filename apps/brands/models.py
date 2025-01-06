from django.db import models


class Brands(models.Model):
    CATEGORY_CHOICES = [
        ('yengil mashina', 'Yengil mashina'),
        ('yuk mashinasi', 'Yuk mashinasi'),
        ('maxsus jihozlar', 'Maxsus jihozlar')
    ]

    RU_CATEGORY_CHOICES = [
        ('легкая машина ', 'Легкая машина'),
        ('грузовик', 'Грузовик'),
        ('специальная техника ', 'Специальная техника ')
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    ru_category = models.CharField(max_length=100, choices=RU_CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    def __str__(self):
        return self.name
