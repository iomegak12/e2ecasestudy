from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username="admin_user").exists():
            User.objects.create_superuser("admin_user", "admin@admin.com", "password")
