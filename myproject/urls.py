from django.contrib import admin
from django.urls import path, include
from . import views
from menu.api_views import MenuItemViewSet, ReservationView, ReservationViewSet

# from reservations.api_views import ReservationView
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'menuitems', MenuItemViewSet, basename='menuitem')
router.register(r'reservations', ReservationViewSet, basename='reservation')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('menu/', include('menu.urls')),
    path('homepage/', views.homepage, name='homepage'),
    path('about/', views.about),
    path('menu_item/', views.menu_item),
    path('accounts/', include('allauth.urls')),
    
    path('api/reservations/', ReservationView.as_view(), name='reservation-list'),
    path('api/reservations/<int:pk>/', ReservationView.as_view(), name='reservation-detail'),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('protected/', views.protected_view, name='protected_view'),

    # Include router URLs
    path('apis/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
# from django.contrib import admin
# from django.urls import path, include
# from . import views
# from menu.api_views import MenuItemViewSet
# from reservations.api_views import ReservationView
# from rest_framework import routers
# from rest_framework.routers import DefaultRouter

# router = routers.DefaultRouter()

# router.register(r'menuitems', MenuItemViewSet)
# router.register(r'reservations', ReservationView, basename='reservation')


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('users.urls')),
#     path('reservations/', include('reservations.urls')),
#     path('menu/', include('menu.urls'), ),
#     path('homepage/', views.homepage),
#     path('about/', views.about),
#     path('menu_item/', views.menu_item ),
#     path('accounts/', include('allauth.urls')),
    
#     path('api-menuItem', MenuItemViewSet.as_view({'get': 'list'}), name='menuItem'),
#     path('api-reservation', ReservationView.as_view(), name='reservation'),

    
    
#     path('apis/', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]
