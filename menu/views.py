from django.shortcuts import render, get_object_or_404, redirect
from .models import MenuItem
from .forms import MenuItemForm
from .decorators import login_required

@login_required
def menu_list(request):
    items = MenuItem.objects.all()
    return render(request, 'menu/menu_list.html', {'items': items})

def menu_detail(request, pk):
    item = get_object_or_404(MenuItem, pk=pk)
    return render(request, 'menu/menu_detail.html', {'item': item})

def menu_create(request):
    if request.method == "POST":
        form = MenuItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect('menu_detail', pk=item.pk)
    else:
        form = MenuItemForm()
    return render(request, 'menu/menu_form.html', {'form': form})

def menu_update(request, pk):
    item = get_object_or_404(MenuItem, pk=pk)
    if request.method == "POST":
        form = MenuItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            return redirect('menu_detail', pk=item.pk)
    else:
        form = MenuItemForm(instance=item)
    return render(request, 'menu/menu_form.html', {'form': form})

def menu_delete(request, pk):
    item = get_object_or_404(MenuItem, pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect('menu_list')
    return render(request, 'menu/menu_confirm_delete.html', {'item': item})
