# myapp/views.py
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import SignUpForm
from .models import Profile
from django.contrib.auth import logout
from django.urls import reverse
from menu.models import Order
from django.shortcuts import render
from menu.models import Order
from menu.forms import OrderForm

def home(request):
    return render(request, 'home.html')

# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             messages.success(request, 'Account created successfully!')
#             return redirect('home')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})

# def signin(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, 'Logged in successfully!')
#                 return redirect('home')
#             else:
#                 messages.error(request, 'Invalid username or password.')
#         else:
#             messages.error(request, 'Invalid username or password.')
#     form = AuthenticationForm()
#     return render(request, 'signin.html', {'form': form})

# def signout(request):
#     logout(request)
#     messages.success(request, 'Logged out successfully!')
#     return redirect('signin')



def profile_page(request, username=None):

    user = get_object_or_404(User, username=username)

    obj = get_object_or_404(Profile, user=user)
    orders = Order.objects.filter(author_of_order=user)
    context = {
        "obj": obj,
        "orders":orders
    }
    return render(request, "profile_page.html", context)


def custom_logout(request):
    logout(request)
    return redirect(reverse('home'))

# profile/views.py

def profile(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user  # Привязка заказа к текущему пользователю, если необходимо
            order.save()
            return redirect('profile')
    else:
        form = OrderForm()
    
    orders = Order.objects.filter(user=request.user)  # Фильтрация заказов для текущего пользователя
    return render(request, 'users/profile_page.html', {'orders': orders, 'form': form})
