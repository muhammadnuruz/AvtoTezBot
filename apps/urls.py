from django.urls import path, include


urlpatterns = [
    path('spare_parts/', include("apps.spare_parts.urls")),
    path('telegram-users/', include("apps.telegram_users.urls")),
    path('types/', include("apps.brands.urls")),
]
