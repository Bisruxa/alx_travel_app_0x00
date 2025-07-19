from django.core.management.base import BaseCommand
from listings.models import Listing
from faker import Faker
import random

class Command(BaseCommand):
    help = "Seeds the database with sample listing data."

    def handle(self, *args, **kwargs):
        fake = Faker()
        self.stdout.write("Seeding data...")

        for _ in range(10):  # Create 10 sample listings
            Listing.objects.create(
                title=fake.company(),
                description=fake.text(),
                price_per_night=round(random.uniform(50, 500), 2),
                location=fake.city(),
                available=True
            )

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))
