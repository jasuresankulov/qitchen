from django.urls import path
from . import views
from .api_views import menuItem_view, MenuItemView


urlpatterns = [
    path('', views.menu_list, name='menu_list'),
    path('menu/<int:pk>/', views.menu_detail, name='menu_detail'),
    path('menu/new/', views.menu_create, name='menu_create'),
    path('menu/<int:pk>/edit/', views.menu_update, name='menu_update'),
    path('menu/<int:pk>/delete/', views.menu_delete, name='menu_delete'),
    
    path('api-menuItem', menuItem_view, name='menuItem'),
    path('api-menuItem-class', MenuItemView.as_view(), name='menuItem-class'),

]
