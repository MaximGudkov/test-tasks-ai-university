import os
from datetime import timedelta

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings")

app = Celery("src")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "collect-data-every-hour": {
        "task": "mystats.tasks.collect_data",
        "schedule": crontab(minute=0, hour="*"),
    },
}
