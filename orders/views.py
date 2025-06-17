from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.db import transaction
from cart.models import Cart, CartItem
from .models import Order, OrderItem
from .forms import CheckoutForm

def is_admin(user):
    return user.is_authenticated and (user.is_staff or user.userprofile.is_admin)

@login_required
def checkout(request):
    """Checkout process to create an order from cart"""
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all()
    
    if not cart_items.exists():
        messages.warning(request, 'Your cart is empty.')
        return redirect('services:item_list')
    
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                # Create order
                order = Order.objects.create(
                    customer=request.user,
                    total_amount=cart.total_price,
                    customer_name=form.cleaned_data['customer_name'],
                    customer_phone=form.cleaned_data['customer_phone'],
                    customer_email=form.cleaned_data['customer_email'],
                    customer_address=form.cleaned_data['customer_address'],
                    pickup_address=form.cleaned_data['pickup_address'],
                    delivery_address=form.cleaned_data['delivery_address'],
                    pickup_date=form.cleaned_data['pickup_date'],
                    delivery_date=form.cleaned_data['delivery_date'],
                )
                
                # Create order items from cart items
                for cart_item in cart_items:
                    OrderItem.objects.create(
                        order=order,
                        item=cart_item.item,
                        service=cart_item.service,
                        quantity=cart_item.quantity,
                        price_per_item=cart_item.service.price,
                    )
                
                # Clear the cart
                cart.cartitem_set.all().delete()
                
                messages.success(request, f'Order placed successfully! Order number: {order.order_number}')
                return redirect('orders:order_detail', order_id=order.id)
    else:
        # Pre-fill form with user data
        initial_data = {
            'customer_name': request.user.get_full_name() or request.user.username,
            'customer_email': request.user.email,
            'customer_phone': getattr(request.user.userprofile, 'phone', ''),
            'customer_address': getattr(request.user.userprofile, 'address', ''),
        }
        form = CheckoutForm(initial=initial_data)
    
    context = {
        'cart': cart,
        'cart_items': cart_items,
        'form': form,
    }
    return render(request, 'orders/checkout.html', context)

@login_required
def order_list(request):
    """Display user's order history"""
    orders = Order.objects.filter(customer=request.user).order_by('-created_at')
    context = {
        'orders': orders,
    }
    return render(request, 'orders/order_list.html', context)

@login_required
def order_detail(request, order_id):
    """Display detailed information about a specific order"""
    order = get_object_or_404(Order, id=order_id, customer=request.user)
    order_items = order.orderitem_set.all()
    
    context = {
        'order': order,
        'order_items': order_items,
    }
    return render(request, 'orders/order_detail.html', context)

@user_passes_test(is_admin)
def admin_order_list(request):
    """Admin view to manage all orders"""
    orders = Order.objects.all().order_by('-created_at')
    
    # Filter by status
    status_filter = request.GET.get('status')
    if status_filter:
        orders = orders.filter(status=status_filter)
    
    context = {
        'orders': orders,
        'status_choices': Order.STATUS_CHOICES,
        'selected_status': status_filter,
    }
    return render(request, 'orders/admin_order_list.html', context)

@user_passes_test(is_admin)
def admin_order_detail(request, order_id):
    """Admin view for detailed order information"""
    order = get_object_or_404(Order, id=order_id)
    order_items = order.orderitem_set.all()
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(Order.STATUS_CHOICES):
            order.status = new_status
            order.save()
            messages.success(request, f'Order status updated to {order.get_status_display()}')
            return redirect('orders:admin_order_detail', order_id=order.id)
    
    context = {
        'order': order,
        'order_items': order_items,
        'status_choices': Order.STATUS_CHOICES,
    }
    return render(request, 'orders/admin_order_detail.html', context)
