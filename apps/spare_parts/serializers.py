from rest_framework import serializers
from .models import SpareParts


class SparePartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpareParts
        fields = '__all__'
