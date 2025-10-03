from django.shortcuts import render
from cars.models import Car # Make sure to import the Car model

def home_view(request):
    # Fetch 6 available cars to feature on the homepage
    featured_cars = Car.objects.filter(is_available=True)[:6] 
    
    # Pass the cars to the template in the context dictionary
    context = {
        'featured_cars': featured_cars
    }
    return render(request, 'core/home.html', context)

def about_view(request):
    return render(request, 'core/about.html')