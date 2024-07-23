from django.shortcuts import render

 
def homepage(request):
    return render(request, 'homepage.html')

def about(request):
    return render(request, 'about.html')

def menu_item(request):
    return render(request, 'menu_item.html')

 