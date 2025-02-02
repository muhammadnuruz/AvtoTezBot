from rest_framework.generics import ListAPIView
from django.db.models import Q
from rest_framework.permissions import AllowAny

from apps.brands.models import Brands
from apps.brands.serializers import BrandsSerializer


class BrandsDetailViewSet(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = BrandsSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return Brands.objects.filter(
            Q(category__icontains=category.lower()) | Q(ru_category__icontains=category.lower())
        )


class AllBrandsListViewSet(ListAPIView):
    queryset = Brands.objects.all()
    permission_classes = [AllowAny]
    serializer_class = BrandsSerializer
