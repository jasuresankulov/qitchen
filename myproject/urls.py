from django.contrib import admin
from django.urls import path, include
from . import views
from menu.api_views import MenuItemViewSet

from rest_framework import routers
router = routers.DefaultRouter()

router.register(r'menuitem', MenuItemViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('reservations/', include('reservations.urls')),
    path('menu/', include('menu.urls')),
    path('homepage/', views.homepage),
    path('about/', views.about),
    path('menu_item/', views.menu_item ),
    
    path('apis/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
