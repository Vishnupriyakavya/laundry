from django.db import models

# Create your models here.

class Service(models.Model):
    SERVICE_TYPES = [
        ('wash', 'Wash'),
        ('dry_clean', 'Dry Clean'),
        ('iron', 'Iron'),
        ('wash_iron', 'Wash & Iron'),
        ('dry_clean_iron', 'Dry Clean & Iron'),
    ]
    
    name = models.CharField(max_length=100)
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} - {self.get_service_type_display()} (${self.price})"

class Item(models.Model):
    ITEM_TYPES = [
        ('shirt', 'Shirt'),
        ('pants', 'Pants'),
        ('dress', 'Dress'),
        ('saree', 'Saree'),
        ('kurta', 'Kurta'),
        ('suit', 'Suit'),
        ('blazer', 'Blazer'),
        ('jeans', 'Jeans'),
        ('t_shirt', 'T-Shirt'),
        ('sweater', 'Sweater'),
        ('coat', 'Coat'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=100)
    item_type = models.CharField(max_length=20, choices=ITEM_TYPES)
    image = models.ImageField(upload_to='items/', blank=True, null=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
