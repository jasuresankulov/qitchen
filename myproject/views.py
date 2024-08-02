from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from menu.models import MenuItem

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response(data={"message": "This is a protected view!"})


@login_required
def homepage(request):
    return render(request, 'homepage.html')
@login_required
def about(request):
    return render(request, 'about.html')
@login_required
def menu_item(request):
    menu_items = MenuItem.objects.all()
    context = {
        "menu_items":menu_items
    }
    return render(request, 'menu_item.html', {'context': context})

def contacts(request):
    return render(request, 'contacts.html')

 