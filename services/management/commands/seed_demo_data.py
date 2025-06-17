from django.core.management.base import BaseCommand
from services.models import Service, Item
import random

class Command(BaseCommand):
    help = 'Seed the database with demo services and items.'

    def handle(self, *args, **options):
        # Service data
        services_data = [
            {'name': 'Wash', 'service_type': 'wash', 'price': 5.0, 'description': 'Standard washing service.'},
            {'name': 'Dry Clean', 'service_type': 'dry_clean', 'price': 8.0, 'description': 'Professional dry cleaning.'},
            {'name': 'Iron', 'service_type': 'iron', 'price': 3.0, 'description': 'Crisp ironing for your clothes.'},
            {'name': 'Wash & Iron', 'service_type': 'wash_iron', 'price': 7.0, 'description': 'Wash and iron combo.'},
            {'name': 'Dry Clean & Iron', 'service_type': 'dry_clean_iron', 'price': 10.0, 'description': 'Dry clean and iron combo.'},
            {'name': 'Fold Only', 'service_type': 'fold', 'price': 2.0, 'description': 'Neat folding service.'},
            {'name': 'Express Wash', 'service_type': 'wash', 'price': 12.0, 'description': 'Same-day express wash.'},
            {'name': 'Premium Care', 'service_type': 'dry_clean', 'price': 15.0, 'description': 'Premium fabric care.'},
        ]

        # Item data
        items_data = [
            {'name': 'Shirt', 'item_type': 'shirt', 'description': 'Cotton or synthetic shirts.'},
            {'name': 'Trousers', 'item_type': 'trousers', 'description': 'Formal and casual trousers.'},
            {'name': 'Saree', 'item_type': 'saree', 'description': 'Delicate sarees of all fabrics.'},
            {'name': 'Blazer', 'item_type': 'blazer', 'description': 'Woolen and formal blazers.'},
            {'name': 'Blanket', 'item_type': 'blanket', 'description': 'Single and double blankets.'},
            {'name': 'Curtains', 'item_type': 'curtain', 'description': 'Window and door curtains.'},
            {'name': 'T-Shirt', 'item_type': 'tshirt', 'description': 'Casual t-shirts.'},
            {'name': 'Jeans', 'item_type': 'jeans', 'description': 'All types of jeans.'},
            {'name': 'Jacket', 'item_type': 'jacket', 'description': 'Winter and rain jackets.'},
            {'name': 'Dress', 'item_type': 'dress', 'description': 'Party and casual dresses.'},
            {'name': 'Skirt', 'item_type': 'skirt', 'description': 'Short and long skirts.'},
            {'name': 'Dupatta', 'item_type': 'dupatta', 'description': 'Light and heavy dupattas.'},
            {'name': 'Bed Sheet', 'item_type': 'bedsheet', 'description': 'Single and double bed sheets.'},
            {'name': 'Pillow Cover', 'item_type': 'pillow_cover', 'description': 'Soft pillow covers.'},
            {'name': 'Towel', 'item_type': 'towel', 'description': 'Bath and hand towels.'},
            {'name': 'Sweater', 'item_type': 'sweater', 'description': 'Woolen sweaters.'},
            {'name': 'Coat', 'item_type': 'coat', 'description': 'Formal and winter coats.'},
            {'name': 'Scarf', 'item_type': 'scarf', 'description': 'Fashionable scarves.'},
        ]

        # Create services
        for s in services_data:
            obj, created = Service.objects.get_or_create(
                name=s['name'],
                defaults={
                    'service_type': s['service_type'],
                    'price': s['price'],
                    'description': s['description'],
                    'is_active': True,
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created service: {obj.name}"))
            else:
                self.stdout.write(f"Service already exists: {obj.name}")

        # Create items
        for i in items_data:
            obj, created = Item.objects.get_or_create(
                name=i['name'],
                defaults={
                    'item_type': i['item_type'],
                    'description': i['description'],
                    'is_active': True,
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created item: {obj.name}"))
            else:
                self.stdout.write(f"Item already exists: {obj.name}")

        self.stdout.write(self.style.SUCCESS('Seeding complete!')) 