from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from advertisements.permissions import IsAdminOrOwner
from advertisements.filters import AdvertisementFilter


class AdvertisementViewSet(viewsets.ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = AdvertisementFilter
    ordering_fields = ['created_at']

    def get_permissions(self):
        """
        Переопределение доступов для отдельных методов.
        """
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminOrOwner()]
        return super().get_permissions()