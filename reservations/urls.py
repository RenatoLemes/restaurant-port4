from django.urls import path
from . import views

urlpatterns = [
    path('reservations/', views.make_reservation, name='make_reservation'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]