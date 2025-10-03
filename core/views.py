from django.shortcuts import render
from cars.models import Car

def home_view(request):
    # Fetch 6 available cars to feature on the homepage
    featured_cars = Car.objects.filter(is_available=True)[:6] 
    
    context = {
        'featured_cars': featured_cars
    }
    return render(request, 'core/home.html', context)

def about_view(request):
    return render(request, 'core/about.html')

def list_car_view(request):
    # For now, this just renders a simple template.
    # Later, you can add a form here.
    return render(request, 'core/list_car.html')