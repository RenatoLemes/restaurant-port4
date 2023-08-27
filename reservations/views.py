from django.shortcuts import render, get_object_or_404
from .models import Table, Reservation
from .forms import ReservationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.views import generic, View


def home(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('make_reservation')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('make_reservation')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def is_customer(user):
    return user.groups.filter(name='Customer').exists()

def is_staff(user):
    return user.groups.filter(name='Staff').exists()

def is_manager(user):
    return user.groups.filter(name='Manager').exists()

#@login_required
#@user_passes_test(is_customer, login_url='not_customer')
def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation_success')  # Create this URL/view for the success page
    else:
        form = ReservationForm()
    return render(request, 'make_reservation.html', {'form': form})
