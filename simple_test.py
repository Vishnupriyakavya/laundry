#!/usr/bin/env python
"""
Simple test to verify logout and cart functionality
"""
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'la2.settings')
django.setup()

from django.test import Client
from django.contrib.auth.models import User
from cart.models import Cart, CartItem
from services.models import Item, Service

def test_basic_functionality():
    """Test basic logout and cart functionality"""
    print("Testing Basic Functionality...")
    
    # Create a test client
    client = Client()
    
    # Get or create a test user
    user, created = User.objects.get_or_create(
        username='testuser',
        defaults={'email': 'test@example.com'}
    )
    if created:
        user.set_password('testpass123')
        user.save()
        print(f"Created test user: {user.username}")
    else:
        print(f"Using existing test user: {user.username}")
    
    # Test login
    login_success = client.login(username='testuser', password='testpass123')
    if login_success:
        print("✅ Login successful")
    else:
        print("❌ Login failed")
        return
    
    # Test logout
    print("\nTesting logout...")
    logout_response = client.get('/accounts/logout/')
    print(f"Logout status: {logout_response.status_code}")
    
    if logout_response.status_code == 302:
        print("✅ Logout successful (redirected)")
        print(f"Redirected to: {logout_response.url}")
    else:
        print("❌ Logout failed")
        print(f"Response content: {logout_response.content[:200]}...")
    
    # Test cart functionality
    print("\nTesting cart functionality...")
    
    # Login again for cart test
    client.login(username='testuser', password='testpass123')
    
    # Get or create cart
    cart, created = Cart.objects.get_or_create(user=user)
    if created:
        print("Created new cart")
    else:
        print("Using existing cart")
    
    # Get some items and services
    items = Item.objects.filter(is_active=True)[:1]
    services = Service.objects.filter(is_active=True)[:1]
    
    if items and services:
        item = items[0]
        service = services[0]
        
        # Add item to cart
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            item=item,
            service=service,
            defaults={'quantity': 2}
        )
        if created:
            print(f"Added {cart_item.quantity}x {item.name}")
        else:
            cart_item.quantity = 2
            cart_item.save()
            print(f"Updated {cart_item.quantity}x {item.name}")
        
        # Test cart totals
        print(f"Cart total items: {cart.total_items}")
        print(f"Cart total price: ${cart.total_price}")
        
        # Test context processor
        from la2.context_processors import cart_processor
        from django.test import RequestFactory
        
        factory = RequestFactory()
        request = factory.get('/')
        request.user = user
        
        context = cart_processor(request)
        print(f"Context processor cart count: {context['cart_count']}")
        print(f"Context processor cart total: ${context['cart_total']}")
        
        if cart.total_items == context['cart_count']:
            print("✅ Cart count matches")
        else:
            print("❌ Cart count doesn't match")
    else:
        print("No items or services found for testing")
    
    print("\nTest completed!")

if __name__ == '__main__':
    test_basic_functionality() 