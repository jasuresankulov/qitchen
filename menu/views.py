from django.shortcuts import render, get_object_or_404, redirect
from .models import MenuItem, Order, Reservation
from .forms import MenuItemForm, ReservationForm, OrderForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from .serializers import OrderSerializer
from .forms import OrderForm

@login_required
def menu_list(request):
    items = MenuItem.objects.all()
    return render(request, 'menu/menu_list.html', {'items': items})

def menu_detail(request, pk):
    item = get_object_or_404(MenuItem, pk=pk)
    return render(request, 'menu/menu_detail.html', {'item': item})
@login_required
def menu_create(request):
    if request.user.username != 'admin':
        return redirect('homepage')

    if request.method == "POST":
        form = MenuItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save()
            return redirect('menu_item')
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
@login_required
def menu_delete(request, pk):
    item = get_object_or_404(MenuItem, pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect('menu_list')
    return render(request, 'menu/menu_confirm_delete.html', {'item': item})

# =============================RESERVATION=========================================================



def make_reservation(request):
    # Your view logic here
    return render(request, 'make_reservation.html')

def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reservation made successfully!')
            return redirect('homepage')
    else:
        form = ReservationForm()
    return render(request, 'reservations/make_reservation.html', {'form': form})
def reservation_success(request):
    return render(request, 'reservations/reservation_success.html')


# ==============================================================================================


class CreateOrderView(APIView):
    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author_of_order=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderListCreate(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

def order_list_view(request):
    orders = Order.objects.all()
    return render(request, 'menu/order_list.html', {'orders': orders})

def order_detail_view(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'menu/order_detail.html', {'order': order})

def order_create_view(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.author_of_order = request.user  # Set the author_of_order field
            order.save()
            return redirect('myorders')
    else:
        form = OrderForm()
    return render(request, 'menu/order_form.html', {'form': form})

# ==========================================================================================

def profile_page(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = OrderForm()
    
    orders = Order.objects.all()
    return render(request, 'users/profile/profile_page.html', {'orders': orders, 'form': form})

def order_edit_view(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('myorders')
    else:
        form = OrderForm(instance=order)
    return render(request, 'menu/order_form.html', {'form': form, 'edit': True})

def order_delete_view(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        order.delete()
        return redirect('myorders')
    return render(request, 'menu/order_confirm_delete.html', {'order': order})

def myorders_view(request):
    orders = Order.objects.filter(author_of_order=request.user)  # Фильтруйте заказы для текущего пользователя
    return render(request, 'menu/myorders.html', {'orders': orders})
# =============================================================================

# @login_required
# def order_dish(request, menuitem_id):
#     menuItem = get_object_or_404(MenuItem, id=menuitem_id)
#     order = None
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             order = form.save(commit = False)
#             order.menuItem = menuItem
#             order.user = request.user
#             order.total_price = menuItem * order.quantity
#             order.save()
#             return redirect('menu_list')
#     else:
#         form = OrderForm()
#     return render(request, 'order_menuItem.html', {'menuItem': menuItem, 'form': form, 'order': order})   

# @login_required
# def user_order_list(request):
#     orders = Order.objects.filter(user=request.user)         
#     return render(request, 'orders.html', {'orders': orders})            
        