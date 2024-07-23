from django.shortcuts import render, redirect
from .forms import ReservationForm

def make_reservation(request):
    # Your view logic here
    return render(request, 'reservations/make_reservation.html')

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
