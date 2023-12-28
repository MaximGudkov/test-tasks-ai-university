from django_filters import rest_framework as filters
from .models import StatisticData


class StatisticDataFilterSet(filters.FilterSet):
    date__gte = filters.DateTimeFilter(field_name='date', lookup_expr='gte')
    date__lte = filters.DateTimeFilter(field_name='date', lookup_expr='lte')

    class Meta:
        model = StatisticData
        fields = []
