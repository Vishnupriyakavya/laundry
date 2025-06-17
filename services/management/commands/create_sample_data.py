from django.core.management.base import BaseCommand
from services.models import Service, Item

class Command(BaseCommand):
    help = 'Create sample services and items for the laundry management system'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')
        
        # Create services
        services_data = [
            {
                'name': 'Basic Wash',
                'service_type': 'wash',
                'price': 5.00,
                'description': 'Standard washing service for everyday clothes'
            },
            {
                'name': 'Premium Wash & Iron',
                'service_type': 'wash_iron',
                'price': 8.00,
                'description': 'Complete washing and ironing service'
            },
            {
                'name': 'Dry Clean',
                'service_type': 'dry_clean',
                'price': 12.00,
                'description': 'Professional dry cleaning for delicate fabrics'
            },
            {
                'name': 'Dry Clean & Press',
                'service_type': 'dry_clean_iron',
                'price': 15.00,
                'description': 'Dry cleaning with professional pressing'
            },
            {
                'name': 'Iron Only',
                'service_type': 'iron',
                'price': 3.00,
                'description': 'Professional ironing service for clean clothes'
            },
        ]
        
        for service_data in services_data:
            service, created = Service.objects.get_or_create(
                name=service_data['name'],
                defaults=service_data
            )
            if created:
                self.stdout.write(f'Created service: {service.name}')
            else:
                self.stdout.write(f'Service already exists: {service.name}')
        
        # Create items
        items_data = [
            {
                'name': 'Cotton Shirt',
                'item_type': 'shirt',
                'description': 'Regular cotton shirt for everyday wear'
            },
            {
                'name': 'Formal Shirt',
                'item_type': 'shirt',
                'description': 'Professional formal shirt for business wear'
            },
            {
                'name': 'Jeans',
                'item_type': 'jeans',
                'description': 'Denim jeans for casual wear'
            },
            {
                'name': 'Dress Pants',
                'item_type': 'pants',
                'description': 'Formal dress pants for professional attire'
            },
            {
                'name': 'Summer Dress',
                'item_type': 'dress',
                'description': 'Light summer dress for casual occasions'
            },
            {
                'name': 'Silk Saree',
                'item_type': 'saree',
                'description': 'Elegant silk saree for special occasions'
            },
            {
                'name': 'Cotton Kurta',
                'item_type': 'kurta',
                'description': 'Traditional cotton kurta for casual wear'
            },
            {
                'name': 'Business Suit',
                'item_type': 'suit',
                'description': 'Professional business suit for formal occasions'
            },
            {
                'name': 'Blazer',
                'item_type': 'blazer',
                'description': 'Formal blazer for professional wear'
            },
            {
                'name': 'T-Shirt',
                'item_type': 't_shirt',
                'description': 'Casual cotton t-shirt for everyday wear'
            },
            {
                'name': 'Sweater',
                'item_type': 'sweater',
                'description': 'Warm sweater for cold weather'
            },
            {
                'name': 'Winter Coat',
                'item_type': 'coat',
                'description': 'Heavy winter coat for extreme cold'
            },
        ]
        
        for item_data in items_data:
            item, created = Item.objects.get_or_create(
                name=item_data['name'],
                defaults=item_data
            )
            if created:
                self.stdout.write(f'Created item: {item.name}')
            else:
                self.stdout.write(f'Item already exists: {item.name}')
        
        self.stdout.write(
            self.style.SUCCESS('Successfully created sample data!')
        ) 