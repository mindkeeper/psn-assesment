"""
Django command to wait db to be available
"""
import time
from MySQLdb import OperationalError as MySQLdbOperationalError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("waiting for database...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=["default"])
                db_up = True
            except (OperationalError, MySQLdbOperationalError):
                self.stdout.write("database unavaiable, waiting 1 second...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database Ready"))
