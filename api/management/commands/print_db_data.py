from django.core.management.base import BaseCommand
from api.models import MiningData

class Command(BaseCommand):
    help = 'Prints all entries from the MiningData table'
    def handle(self, *args, **kwargs):
        mining_data_entries = MiningData.objects.all()
        if mining_data_entries:
            self.stdout.write(self.style.SUCCESS("MiningData entries:"))
            for entry in mining_data_entries:
                self.stdout.write(f"- Date: {entry.date}, Time: {entry.time}, Latitude: {entry.location_latitude}, Longitude: {entry.location_longitude}, Cu Grade: {entry.cu_grade}")
        else:
            self.stdout.write(self.style.WARNING("No entries found in the MiningData table."))
