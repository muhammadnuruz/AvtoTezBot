from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from apps.spare_parts.models import SpareParts
from apps.spare_parts.serializers import SparePartsSerializer


class SparePartsDetailView(ListAPIView):
    queryset = SpareParts.objects.all()
    serializer_class = SparePartsSerializer
    permission_classes = [AllowAny]
