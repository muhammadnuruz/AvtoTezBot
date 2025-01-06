from django.urls import path

from apps.brands.views import BrandsDetailViewSet

urlpatterns = [
    path('filter/<str:category>/', BrandsDetailViewSet.as_view(),
         name='filter-brands'),
]
