from django.db import models


class TelegramUsers(models.Model):
    LANGUAGE_CHOICES = [
        ('ru', 'Русский'),  # Русский uchun
        ('uz', 'Узбекский'),  # Узбекский uchun
    ]
    chat_id = models.CharField("Чат ID", max_length=255, unique=True)
    username = models.CharField("Имя пользователя", max_length=255, null=True)
    full_name = models.CharField("Полное имя", max_length=255)
    city = models.CharField("Город", max_length=20, default='Toshkent')  # Toshkent ruschasiga Tашкент
    language = models.CharField("Язык", max_length=2, choices=LANGUAGE_CHOICES, default='uz')
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    class Meta:
        verbose_name = "Пользователь Telegram"
        verbose_name_plural = "Пользователи Telegram"

    def __str__(self):
        return f"{self.full_name}"
