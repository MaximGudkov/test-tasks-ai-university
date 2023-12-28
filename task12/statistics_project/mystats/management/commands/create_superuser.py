import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        if (username := os.getenv("SUPERUSER_USERNAME")) and (
            password := os.getenv("SUPERUSER_PASSWORD")
        ):
            self.stdout.write("Creating superuser...")

            User = get_user_model()
            if User.objects.filter(username=username).exists():
                self.stdout.write(self.style.SUCCESS("Superuser already exists"))
            else:
                User.objects.create_superuser(username=username, password=password)
                self.stdout.write(self.style.SUCCESS("Superuser created successfully"))
