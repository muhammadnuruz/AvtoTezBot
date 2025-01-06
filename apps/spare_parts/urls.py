from django.urls import path

from apps.spare_parts.views import SparePartsDetailView

urlpatterns = [
    path('', SparePartsDetailView.as_view(), name='spare-parts-list'),
]
