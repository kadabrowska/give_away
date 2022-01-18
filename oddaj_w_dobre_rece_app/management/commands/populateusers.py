from django.core.management.base import BaseCommand
from ._private import create_users


class Command(BaseCommand):
    help = 'Populates database with users'

    def handle(self, *args, **options):
        create_users()
        self.stdout.write(self.style.SUCCESS("Successfully populated database with users"))
