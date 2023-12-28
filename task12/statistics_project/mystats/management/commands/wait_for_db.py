from time import sleep

from django.core.management.base import BaseCommand
from django.db import connection
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_conn = None
        while not db_conn:
            try:
                connection.ensure_connection()
                db_conn = True
            except OperationalError as e:
                self.stdout.write(f"Database unavailable, waiting 10 second... {e}")
                sleep(10)

        self.stdout.write(self.style.SUCCESS("Database available!"))
