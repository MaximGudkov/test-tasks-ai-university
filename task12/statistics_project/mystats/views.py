from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import StatisticData
from .serializers import StatisticDataSerializer
from .filters import StatisticDataFilterSet


class StatisticDataView(generics.ListAPIView):
    queryset = StatisticData.objects.all()
    serializer_class = StatisticDataSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = StatisticDataFilterSet
