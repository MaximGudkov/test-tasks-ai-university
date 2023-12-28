FROM python:3.11-alpine3.15

WORKDIR /usr/src/statistics_project

COPY ./statistics_project/requirements.txt .
RUN pip install -r requirements.txt

COPY ./docker/dev/statistics_project/entrypoint.sh /
COPY ./statistics_project .

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]