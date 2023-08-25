from django.shortcuts import render, get_object_or_404
from .models import Table, Reservation
from .forms import ReservationForm


def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation_success')  # Create this URL/view for the success page
    else:
        form = ReservationForm()
    return render(request, 'make_reservation.html', {'form': form})