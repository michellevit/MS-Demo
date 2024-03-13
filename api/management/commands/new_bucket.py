from django.core.management.base import BaseCommand
import os
import django
import random
from datetime import datetime, timedelta
from api.models import MiningData
from decimal import Decimal

# Initialize Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoapp.settings")
django.setup()

class Command(BaseCommand):
    help = 'Generate mining data and create a new entry in the MiningData table'

    def handle(self, *args, **options):
        # Get current date and time
        current_date = datetime.now().date()
        current_time = datetime.now().time()

        # Get the latest MiningData entry
        latest_entry = MiningData.objects.order_by('-id').first()

        # Initialize latitude and longitude variables
        if latest_entry:
            prev_latitude = latest_entry.location_latitude
            prev_longitude = latest_entry.location_longitude
        else:
            # If no previous entry exists, use default coordinates
            prev_latitude, prev_longitude = Decimal('49.3926'), Decimal('-120.5526')  # Coordinates of Copper Mountain Mine

        # Generate random latitude and longitude within a certain range from the previous point
        # You can adjust the range based on your requirements
        latitude_range = (float(prev_latitude - Decimal('0.01')), float(prev_latitude + Decimal('0.01')))
        longitude_range = (float(prev_longitude - Decimal('0.01')), float(prev_longitude + Decimal('0.01')))

        # Generate random coordinates
        new_latitude = random.uniform(latitude_range[0], latitude_range[1])
        new_longitude = random.uniform(longitude_range[0], longitude_range[1])

        # Generate random Cu grade between 0 and 1%
        cu_grade = random.uniform(0, 1)

        # Create new MiningData entry
        mining_data = MiningData.objects.create(
            date=current_date,
            time=current_time,
            location_latitude=new_latitude,
            location_longitude=new_longitude,
            cu_grade=cu_grade
        )

        # Print data
        self.stdout.write(self.style.SUCCESS("New mining data entry created:"))
        self.stdout.write(f"- Date: {current_date}")
        self.stdout.write(f"- Time: {current_time}")
        self.stdout.write(f"- Location Latitude: {new_latitude}")
        self.stdout.write(f"- Location Longitude: {new_longitude}")
        self.stdout.write(f"- Cu Grade: {cu_grade}")
