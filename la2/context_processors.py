from cart.models import Cart

def cart_processor(request):
    """Context processor to make cart information available globally"""
    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(user=request.user)
            # Force calculation of totals by querying the database directly
            cart_items = cart.cartitem_set.all()
            total_items = sum(item.quantity for item in cart_items)
            total_price = sum(item.service.price * item.quantity for item in cart_items)
            
            # Debug output (remove in production)
            # print(f"Cart processor: {total_items} items, ${total_price} for user {request.user.username}")
            
            return {
                'cart_count': total_items,
                'cart_total': total_price,
            }
        except Cart.DoesNotExist:
            return {
                'cart_count': 0,
                'cart_total': 0,
            }
    return {
        'cart_count': 0,
        'cart_total': 0,
    } 