from django.urls import path

from apps.contacts.views import ContactsDetailViewSet

urlpatterns = [
    path('filter/<str:brand>/<str:spare_parts>/', ContactsDetailViewSet.as_view(),
         name='filter-contacts'),
]
