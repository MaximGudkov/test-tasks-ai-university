from django.db import models


class StatisticData(models.Model):
    data = models.JSONField()
    date = models.DateField(auto_now_add=True)
