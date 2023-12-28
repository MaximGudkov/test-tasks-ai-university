import requests
from celery import shared_task
from django.conf import settings

from .models import StatisticData


@shared_task
def collect_data():
    api_key = settings.API_KEY
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&apikey={api_key}"

    response = requests.get(url)
    data = response.json()

    StatisticData.objects.create(data=data)
