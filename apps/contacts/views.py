from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from apps.contacts.models import Contacts
from apps.contacts.serializers import ContactsSerializer


class ContactsDetailViewSet(APIView):
    def get(self, request, brand, spare_part):
        contacts = Contacts.objects.filter(
            Q(brands__name__icontains=brand) |
            Q(brands__ru_category__icontains=brand) |
            Q(spare_parts__name__icontains=spare_part) |
            Q(spare_parts__ru_name__icontains=spare_part)
        ).distinct()

        serializer = ContactsSerializer(contacts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
