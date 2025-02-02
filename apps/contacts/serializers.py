from rest_framework import serializers
from apps.contacts.models import Contacts


class ContactsSerializer(serializers.ModelSerializer):
    brands = serializers.StringRelatedField(many=True)
    spare_parts = serializers.StringRelatedField(many=True)

    class Meta:
        model = Contacts
        fields = (
            'id', 'name', 'address', 'landmark', 'phone_number', 'brands', 'spare_parts', 'created_at', 'updated_at')
