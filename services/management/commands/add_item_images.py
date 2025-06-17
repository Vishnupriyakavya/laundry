from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from services.models import Item
import requests
import os
from urllib.parse import urlparse

class Command(BaseCommand):
    help = 'Add sample images to items using placeholder images'

    def handle(self, *args, **options):
        # Better and more accurate image URLs for different item types
        item_images = {
            'shirt': 'https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?w=400&h=400&fit=crop',
            'pants': 'https://images.unsplash.com/photo-1544966503-7cc5ac882d5f?w=400&h=400&fit=crop',
            'dress': 'https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=400&h=400&fit=crop',
            'saree': 'https://images.unsplash.com/photo-1583394838336-acd977736f90?w=400&h=400&fit=crop',
            'kurta': 'https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?w=400&h=400&fit=crop',
            'suit': 'https://images.unsplash.com/photo-1593030761757-71fae45fa0e7?w=400&h=400&fit=crop',
            'blazer': 'https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=400&h=400&fit=crop',
            'jeans': 'https://images.unsplash.com/photo-1542272604-787c3835535d?w=400&h=400&fit=crop',
            't_shirt': 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400&h=400&fit=crop',
            'sweater': 'https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=400&h=400&fit=crop',
            'coat': 'https://images.unsplash.com/photo-1551028719-00167b16eac5?w=400&h=400&fit=crop',
            'other': 'https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=400&h=400&fit=crop',
        }

        # Specific images for each item with better accuracy - using working URLs
        specific_images = {
            # Bedding and Home items
            'Bed Sheet': 'https://images.unsplash.com/photo-1585487771212-dbf03dc15555?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
            'Blanket': 'https://images.unsplash.com/photo-1591969245138-091c6e119d67?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
            'Curtains': 'https://images.unsplash.com/photo-1578938171638-34f37803d154?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
            'Pillow Cover': 'https://images.unsplash.com/photo-1517702878411-e40d0499388c?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
            'Towel': 'https://images.unsplash.com/photo-1521666687040-af85a536780c?q=80&w=1935&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
            
            # Women's Clothing
            'Dress': 'https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=400&h=400&fit=crop',
            'Skirt': 'https://images.unsplash.com/photo-1590740924773-193c66060c1d?q=80&w=1935&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
            'Summer Dress': 'https://images.unsplash.com/photo-1588661640243-7f722a468d6c?q=80&w=1935&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
            'Saree': 'https://images.unsplash.com/photo-1583394838336-acd977736f90?w=400&h=400&fit=crop',
            'Silk Saree': 'https://images.unsplash.com/photo-1583394838336-acd977736f90?w=400&h=400&fit=crop',
            'Dupatta': 'https://images.unsplash.com/photo-1621217036667-27b9c9f2b8f8?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
            
            # Men's Formal Wear
            'Shirt': 'https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?w=400&h=400&fit=crop',
            'Formal Shirt': 'https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?w=400&h=400&fit=crop',
            'Cotton Shirt': 'https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?w=400&h=400&fit=crop',
            'Trousers': 'https://images.unsplash.com/photo-1544465548-262174091c53?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
            'Dress Pants': 'https://images.unsplash.com/photo-1512436991641-6745cdb1723f?w=400&h=400&fit=crop',
            'Business Suit': 'https://images.unsplash.com/photo-1593030761757-71fae45fa0e7?w=400&h=400&fit=crop',
            'Blazer': 'https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=400&h=400&fit=crop',
            
            # Casual Wear
            'T-Shirt': 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400&h=400&fit=crop',
            'Jeans': 'https://images.unsplash.com/photo-1542272604-787c3835535d?w=400&h=400&fit=crop',
            
            # Traditional Wear
            'Cotton Kurta': 'https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?w=400&h=400&fit=crop',
            
            # Outerwear
            'Jacket': 'https://images.unsplash.com/photo-1551028719-00167b16eac5?w=400&h=400&fit=crop',
            'Coat': 'https://images.unsplash.com/photo-1551028719-00167b16eac5?w=400&h=400&fit=crop',
            'Winter Coat': 'https://images.unsplash.com/photo-1551028719-00167b16eac5?w=400&h=400&fit=crop',
            'Sweater': 'https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=400&h=400&fit=crop',
            'Scarf': 'https://images.unsplash.com/photo-1598253139360-1e54c8d7b308?q=80&w=1935&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
        }

        items = Item.objects.all()
        
        for item in items:
            # Skip if item already has an image
            if item.image:
                self.stdout.write(f"Item '{item.name}' already has an image, skipping...")
                continue
            
            # Try to get specific image first, then fall back to item type
            image_url = specific_images.get(item.name, item_images.get(item.item_type, item_images['other']))
            
            try:
                # Download the image
                response = requests.get(image_url, timeout=10)
                response.raise_for_status()
                
                # Get file extension from URL
                parsed_url = urlparse(image_url)
                file_extension = os.path.splitext(parsed_url.path)[1] or '.jpg'
                
                # Create filename
                filename = f"{item.name.lower().replace(' ', '_')}{file_extension}"
                
                # Save the image to the item using ContentFile
                item.image.save(filename, ContentFile(response.content), save=True)
                
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully added image to '{item.name}'")
                )
                
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"Failed to add image to '{item.name}': {str(e)}")
                )
        
        self.stdout.write(self.style.SUCCESS('Image addition process completed!')) 