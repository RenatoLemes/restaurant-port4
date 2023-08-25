from django.urls import path
from . import views

urlpatterns = [
    path('reservations/', views.make_reservation, name='make_reservation'),
]