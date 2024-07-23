# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import SignUpForm


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












