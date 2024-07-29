from django.urls import path
from . import views
from .views import *
from .views import *


urlpatterns = [
    path('', menu_list, name='menu_list'),
    path('menu/<int:pk>/', menu_detail, name='menu_detail'),
    path('new/', menu_create, name='menu_create'),
    path('menu/<int:pk>/edit/', menu_update, name='menu_update'),
    path('menu/<int:pk>/delete/', menu_delete, name='menu_delete'),
    
    path('make_reservation/', make_reservation, name='make_reservation',),
    path('reservation_success/', reservation_success, name='reservation_success',),
    
    
    
    path('orders/', OrderListCreate.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetail.as_view(), name='order-detail'),
    path('create-order/', CreateOrderView.as_view(), name='create-order'),
    path('orders-list/', order_list_view, name='order-list-view'),
    path('orders/<int:pk>/detail/', order_detail_view, name='order-detail-view'),
    path('orders/create/', order_create_view, name='order-create-view'),

    path('create/', order_create_view, name='order-create-view'),
    path('profile/', order_create_view, name='profile'),
    path('myorders/', myorders_view, name='myorders'),  # Добавьте путь к myorders
    path('orders/<int:pk>/edit/', order_edit_view, name='order-edit-view'),
    path('orders/<int:pk>/delete/', order_delete_view, name='order-delete-view'),
    # path('order/<int:menuitem_id>/', order_dish, name='order_menuItem'),  
    # path('my_orders/', user_order_list, name='user_order_list'),
]
