# bookings/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('my-bookings/', views.my_bookings_view, name='my_bookings'),
    path('create/<int:car_pk>/', views.create_booking_view, name='create_booking'),
]