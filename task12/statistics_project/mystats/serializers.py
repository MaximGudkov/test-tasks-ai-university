from rest_framework import serializers

from .models import StatisticData


class StatisticDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatisticData
        fields = "__all__"
