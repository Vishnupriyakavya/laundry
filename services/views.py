from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Service, Item

def service_list(request):
    """Display all available services"""
    services = Service.objects.filter(is_active=True)
    context = {
        'services': services,
    }
    return render(request, 'services/service_list.html', context)

def item_list(request):
    """Display all available items"""
    items = Item.objects.filter(is_active=True)
    services = Service.objects.filter(is_active=True)
    
    # Filter by item type if provided
    item_type = request.GET.get('item_type')
    if item_type:
        items = items.filter(item_type=item_type)
    
    # Filter by service type if provided
    service_type = request.GET.get('service_type')
    if service_type:
        services = services.filter(service_type=service_type)
    
    context = {
        'items': items,
        'services': services,
        'item_types': Item.ITEM_TYPES,
        'service_types': Service.SERVICE_TYPES,
        'selected_item_type': item_type,
        'selected_service_type': service_type,
    }
    return render(request, 'services/item_list.html', context)

def item_detail(request, item_id):
    """Display detailed information about a specific item"""
    item = get_object_or_404(Item, id=item_id, is_active=True)
    services = Service.objects.filter(is_active=True)
    
    context = {
        'item': item,
        'services': services,
    }
    return render(request, 'services/item_detail.html', context)
