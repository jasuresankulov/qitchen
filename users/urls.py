# myapp/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    # path('signup/', views.signup, name='signup'),
    # path('signin/', views.signin, name='signin'),
    # path('signout/', views.signout, name='signout'),
    path('', home, name='home'),
    path("profile/<str:username>/", profile_page, name='profile'),
    path('accounts/logout/', custom_logout, name='account_logout'),
]
