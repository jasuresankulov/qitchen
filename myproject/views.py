from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def homepage(request):
    return render(request, 'homepage.html')
@login_required
def about(request):
    return render(request, 'about.html')
@login_required
def menu_item(request):
    return render(request, 'menu_item.html')

 