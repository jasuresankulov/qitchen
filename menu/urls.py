from django.urls import path
from . import views
from .views import OrderListCreate, OrderDetail, CreateOrderView, order_list_view, order_detail_view, order_create_view
from .views import profile_page_view, order_edit_view, order_delete_view


urlpatterns = [
    path('', views.menu_list, name='menu_list'),
    path('menu/<int:pk>/', views.menu_detail, name='menu_detail'),
    path('menu/new/', views.menu_create, name='menu_create'),
    path('menu/<int:pk>/edit/', views.menu_update, name='menu_update'),
    path('menu/<int:pk>/delete/', views.menu_delete, name='menu_delete'),
    
    path('make_reservation/', views.make_reservation, name='make_reservation',),
    path('reservation_success/', views.reservation_success, name='reservation_success',),
    
    
    
    path('orders/', OrderListCreate.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetail.as_view(), name='order-detail'),
    path('create-order/', CreateOrderView.as_view(), name='create-order'),
    path('orders-list/', order_list_view, name='order-list-view'),
    path('orders/<int:pk>/detail/', order_detail_view, name='order-detail-view'),
    path('orders/create/', order_create_view, name='order-create-view'),
    
    
    path('users/', profile_page_view, name='profile-page-view'),
    path('orders/<int:pk>/edit/', order_edit_view, name='order-edit-view'),
    path('orders/<int:pk>/delete/', order_delete_view, name='order-delete-view'),
    # path('order/<int:menuitem_id>/', views.order_dish, name='order_menuItem'),  
    # path('my_orders/', views.user_order_list, name='user_order_list'),
]
