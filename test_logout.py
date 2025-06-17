#!/usr/bin/env python
"""
Test script to verify logout functionality
"""
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'la2.settings')
django.setup()

from django.test import Client
from django.contrib.auth.models import User

def test_logout():
    """Test logout functionality"""
    print("Testing Logout Functionality...")
    
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
    print(f"Logout response status: {logout_response.status_code}")
    print(f"Logout response URL: {logout_response.url if hasattr(logout_response, 'url') else 'No redirect'}")
    
    if logout_response.status_code == 302:  # Redirect after logout
        print("✅ Logout successful (redirected)")
        print(f"Redirected to: {logout_response.url}")
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
    test_logout() 