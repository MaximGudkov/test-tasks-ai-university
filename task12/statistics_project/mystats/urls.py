from django.urls import path

from .views import StatisticDataView

urlpatterns = [
    path("stats/", StatisticDataView.as_view(), name="api-stats"),
]
