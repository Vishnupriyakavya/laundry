from django.core.management.base import BaseCommand
from services.models import Item

class Command(BaseCommand):
    help = 'Clear existing images from items'

    def handle(self, *args, **options):
        items = Item.objects.all()
        
        for item in items:
            if item.image:
                # Delete the image file
                item.image.delete(save=False)
                # Clear the image field
                item.image = None
                item.save()
                self.stdout.write(
                    self.style.SUCCESS(f"Cleared image from '{item.name}'")
                )
            else:
                self.stdout.write(f"Item '{item.name}' has no image to clear")
        
        self.stdout.write(self.style.SUCCESS('Image clearing process completed!')) 