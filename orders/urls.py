from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('', views.order_list, name='order_list'),
    path('<int:order_id>/', views.order_detail, name='order_detail'),
    path('admin/', views.admin_order_list, name='admin_order_list'),
    path('admin/<int:order_id>/', views.admin_order_detail, name='admin_order_detail'),
] 