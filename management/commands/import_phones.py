from django.core.management.base import BaseCommand
import csv
from .models import Phone

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('phones.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                phone = Phone(
                    name=row['name'],
                    price=row['price'],
                    image=row['image'],
                    release_date=row['release_date'],
                    lte_exists=bool(row['lte_exists'])
                )
                phone.save()
        self.stdout.write(self.style.SUCCESS('Data imported successfully!'))
