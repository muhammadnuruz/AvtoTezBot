from django.urls import path

from apps.brands.views import BrandsDetailViewSet, AllBrandsListViewSet

urlpatterns = [
    path('filter/<str:category>/', BrandsDetailViewSet.as_view(),
         name='filter-brands'),
    path('', AllBrandsListViewSet.as_view(),
         name='all-brands'),
]
