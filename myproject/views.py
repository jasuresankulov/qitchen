from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from menu.models import MenuItem

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

 