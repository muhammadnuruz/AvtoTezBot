from rest_framework.generics import ListAPIView
from django.db.models import Q
from .models import Contacts
from .serializers import ContactsSerializer
from rest_framework.permissions import AllowAny


class ContactsDetailViewSet(ListAPIView):
    serializer_class = ContactsSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        brand = self.kwargs["brand"]
        spare_part = self.kwargs["spare_parts"]
        return Contacts.objects.filter(
            Q(brands__name=brand) &
            (Q(spare_parts__name__icontains=spare_part) |
             Q(spare_parts__ru_name__icontains=spare_part))
        ).distinct()
