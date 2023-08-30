from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('make_reservation/', views.make_reservation, name='reservation'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]