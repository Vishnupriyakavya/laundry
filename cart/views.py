from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from services.models import Item, Service
from .models import Cart, CartItem

@login_required
def cart_view(request):
    """Display the user's cart"""
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all()
    
    # Refresh the cart object to get updated totals
    cart.refresh_from_db()
    
    context = {
        'cart': cart,
        'cart_items': cart_items,
    }
    return render(request, 'cart/cart.html', context)

@login_required
def add_to_cart(request):
    """Add an item to the cart"""
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        service_id = request.POST.get('service_id')
        quantity = int(request.POST.get('quantity', 1))
        
        if not item_id or not service_id:
            messages.error(request, 'Please select both item and service.')
            return redirect('services:item_list')
        
        item = get_object_or_404(Item, id=item_id, is_active=True)
        service = get_object_or_404(Service, id=service_id, is_active=True)
        
        cart, created = Cart.objects.get_or_create(user=request.user)
        
        # Check if item with same service already exists in cart
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            item=item,
            service=service,
            defaults={'quantity': quantity}
        )
        
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        
        messages.success(request, f'{quantity}x {item.name} added to cart.')
        return redirect('cart:cart_view')
    
    return redirect('services:item_list')

@login_required
def update_cart_item(request, item_id):
    """Update quantity of a cart item"""
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
        
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
            
        # Refresh the cart object to get updated totals
        cart = Cart.objects.get(user=request.user)
        cart.refresh_from_db()

        response_data = {
            'success': True,
            'item_id': item_id,
            'quantity': cart_item.quantity if quantity > 0 else 0,
            'item_total_price': f'{cart_item.total_price:.2f}' if quantity > 0 else '0.00',
            'cart_total_price': f'{cart.total_price:.2f}',
            'cart_total_items': cart.total_items,
        }
        return JsonResponse(response_data)
    
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)

@login_required
def remove_from_cart(request, item_id):
    """Remove an item from the cart"""
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item_name = cart_item.item.name
    cart_item.delete()
    messages.success(request, f'{item_name} removed from cart.')
    return redirect('cart:cart_view')

@login_required
def clear_cart(request):
    """Clear all items from the cart"""
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart.cartitem_set.all().delete()
    messages.success(request, 'Cart cleared successfully.')
    return redirect('cart:cart_view')
