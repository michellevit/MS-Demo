from django.core.management.base import BaseCommand
from django.db import connection
from api.models import MiningData

class Command(BaseCommand):
    help = 'Clears all entries from specified tables and resets their indexes'

    def handle(self, *args, **kwargs):
        models = [MiningData]

        for model in models:
            # Clear all entries in the table
            model.objects.all().delete()
            self.stdout.write(self.style.SUCCESS(f'Cleared all entries from {model.__name__}'))

            # Reset the primary key sequence (Auto Increment ID)
            with connection.cursor() as cursor:
                table_name = model._meta.db_table
                reset_sql = f"ALTER SEQUENCE {table_name}_id_seq RESTART WITH 1;"
                cursor.execute(reset_sql)
                self.stdout.write(self.style.SUCCESS(f'Reset index for {model.__name__}'))

        self.stdout.write(self.style.SUCCESS('Database tables have been reset successfully.'))
