#!/usr/bin/env python
"""
Simple test script to verify cart and logout functionality
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'la2.settings')
django.setup()

from django.contrib.auth.models import User
from cart.models import Cart, CartItem
from services.models import Item, Service
from django.test import RequestFactory

def test_cart_functionality():
    """Test cart functionality"""
    print("Testing Cart Functionality...")
    
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
    
    # Get or create cart
    cart, created = Cart.objects.get_or_create(user=user)
    if created:
        print("Created new cart")
    else:
        print("Using existing cart")
    
    # Clear existing cart items for clean test
    cart.cartitem_set.all().delete()
    
    # Get some items and services
    items = Item.objects.filter(is_active=True)[:2]
    services = Service.objects.filter(is_active=True)[:2]
    
    if not items or not services:
        print("No items or services found. Please run the management command to populate data.")
        return
    
    print(f"Found {items.count()} items and {services.count()} services")
    
    # Add items to cart
    for i, item in enumerate(items):
        service = services[i % len(services)]
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            item=item,
            service=service,
            defaults={'quantity': i + 1}
        )
        if created:
            print(f"Added {cart_item.quantity}x {item.name} with {service.name}")
        else:
            cart_item.quantity = i + 1
            cart_item.save()
            print(f"Updated {cart_item.quantity}x {item.name} with {service.name}")
    
    # Test cart totals
    print(f"\nCart Summary:")
    print(f"Total Items: {cart.total_items}")
    print(f"Total Price: ${cart.total_price}")
    
    # Test context processor
    from la2.context_processors import cart_processor
    
    factory = RequestFactory()
    request = factory.get('/')
    request.user = user
    
    context = cart_processor(request)
    print(f"\nContext Processor Results:")
    print(f"Cart Count: {context['cart_count']}")
    print(f"Cart Total: ${context['cart_total']}")
    
    # Verify totals match
    if cart.total_items == context['cart_count'] and cart.total_price == context['cart_total']:
        print("✅ Cart totals match between model and context processor")
    else:
        print("❌ Cart totals don't match!")
        print(f"Model: {cart.total_items} items, ${cart.total_price}")
        print(f"Context: {context['cart_count']} items, ${context['cart_total']}")
    
    print("\nTest completed!")

def test_logout_functionality():
    """Test logout functionality"""
    print("\nTesting Logout Functionality...")
    
    from django.contrib.auth import authenticate, login
    from django.test import Client
    
    # Create a test client
    client = Client()
    
    # Get or create a test user
    user, created = User.objects.get_or_create(
        username='logouttest',
        defaults={'email': 'logouttest@example.com'}
    )
    if created:
        user.set_password('testpass123')
        user.save()
        print(f"Created test user: {user.username}")
    else:
        print(f"Using existing test user: {user.username}")
    
    # Test login
    login_success = client.login(username='logouttest', password='testpass123')
    if login_success:
        print("✅ Login successful")
    else:
        print("❌ Login failed")
        return
    
    # Test that user is authenticated
    response = client.get('/')
    if response.status_code == 200:
        print("✅ User is authenticated (can access home page)")
    else:
        print("❌ User authentication failed")
        return
    
    # Test logout
    logout_response = client.get('/accounts/logout/')
    if logout_response.status_code == 302:  # Redirect after logout
        print("✅ Logout successful (redirected)")
    else:
        print(f"❌ Logout failed (status code: {logout_response.status_code})")
    
    # Test that user is no longer authenticated
    response = client.get('/')
    if response.status_code == 200:
        print("✅ User is no longer authenticated")
    else:
        print("❌ User still appears to be authenticated")
    
    print("Logout test completed!")

if __name__ == '__main__':
    test_cart_functionality()
    test_logout_functionality() 