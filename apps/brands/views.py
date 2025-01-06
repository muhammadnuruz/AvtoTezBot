from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from apps.brands.models import Brands
from apps.brands.serializers import BrandsSerializer


class BrandsDetailViewSet(APIView):
    def get(self, request, category):
        brands = Brands.objects.filter(
            Q(category__icontains=category) | Q(ru_category__icontains=category)
        )

        serializer = BrandsSerializer(brands, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
