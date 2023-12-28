# MyStats API - Django-приложение для сбора и предоставления статистики через API.

### Quick start:

- Install "Docker" and "docker compose" on your machine

- Change API_KEY variable in ./docker/dev/env/.statistics_project.env

- `docker-compose up --build` - run the project

- Go to http://0.0.0.0:8000/api/schema/swagger-ui/ to see api docs with swagger

### Usage:

After starting the project superuser would be created:
username=ivan
password=1

You can get data from api using GET request to http://0.0.0.0:8000/api/stats/
- you should authorize (you can do it in swagger)

There are two filters: date_gte, date_lte - to filter data by dates:
- http://0.0.0.0:8000/api/stats/?date__gte=2024-01-01
- http://0.0.0.0:8000/api/stats/?date__lte=2024-01-01