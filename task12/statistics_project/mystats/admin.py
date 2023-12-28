from django.contrib import admin

from . import models


@admin.register(models.StatisticData)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("date",)
