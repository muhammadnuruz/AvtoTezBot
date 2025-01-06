from rest_framework import serializers
from apps.brands.models import Brands


class BrandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brands
        fields = ('id', 'name', 'category', 'ru_category', 'created_at', 'updated_at')
