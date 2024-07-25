from django.shortcuts import render, get_object_or_404, redirect
from .models import MenuItem, Order
from .forms import MenuItemForm, ReservationForm, OrderForm

from django.contrib.auth.decorators import login_required


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



def make_reservation(request):
    # Your view logic here
    return render(request, 'make_reservation.html')

def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation_success')
    else:
        form = ReservationForm()
    return render(request, 'reservations/make_reservation.html', {'form': form})

def reservation_success(request):
    return render(request, 'reservations/reservation_success.html')


@login_required
def order_dish(request, menuitem_id):
    menuItem = get_object_or_404(MenuItem, id=menuitem_id)
    order = None
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit = False)
            order.menuItem = menuItem
            order.user = request.user
            order.total_price = menuItem * order.quantity
            order.save()
            return redirect('menu_list')
    else:
        form = OrderForm()
    return render(request, 'order_menuItem.html', {'menuItem': menuItem, 'form': form, 'order': order})   

@login_required
def user_order_list(request):
    orders = Order.objects.filter(user=request.user)         
    return render(request, 'orders.html', {'orders': orders})            
        