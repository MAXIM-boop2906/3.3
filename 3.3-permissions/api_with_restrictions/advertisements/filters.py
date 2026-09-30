from django_filters import FilterSet, DateFromToRangeFilter
from .models import Advertisement


class AdvertisementFilter(FilterSet):
    created_at = DateFromToRangeFilter(field_name='created_at')

    class Meta:
        model = Advertisement
        fields = ['status', 'created_at']