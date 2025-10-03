from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from .models import Car
from bookings.models import Booking
from django.db.models import Q
from datetime import datetime
from .forms import CarForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def car_list_view(request):
    cars = Car.objects.filter(is_available=True)
    
    # Get search parameters from the URL
    location = request.GET.get('location')
    pickup_date_str = request.GET.get('pickup_date')
    return_date_str = request.GET.get('return_date')

    # If location and dates are provided, filter the cars
    if location and pickup_date_str and return_date_str:
        # Filter by location first
        cars = cars.filter(location__icontains=location)
        
        # Convert date strings to datetime objects
        pickup_date = datetime.strptime(pickup_date_str, '%Y-%m-%d').date()
        return_date = datetime.strptime(return_date_str, '%Y-%m-%d').date()
        
        # Find cars that have conflicting bookings
        # A booking conflicts if its date range overlaps with the requested date range
        conflicting_bookings = Booking.objects.filter(
            Q(pickup_date__lte=return_date) & Q(return_date__gte=pickup_date)
        )
        
        # Get the IDs of the cars that are already booked
        booked_car_ids = conflicting_bookings.values_list('car_id', flat=True)
        
        # Exclude the booked cars from the search results
        cars = cars.exclude(id__in=booked_car_ids)

    context = {
        'cars': cars,
        # You can also pass the search query back to the template to display it
        'query_location': location,
        'query_pickup_date': pickup_date_str,
        'query_return_date': return_date_str,
    }
    return render(request, 'cars/car_list.html', context)

def car_list_view(request):
    query = request.GET.get('q', '') # For the search bar
    if query:
        cars = Car.objects.filter(brand__icontains=query) | Car.objects.filter(model__icontains=query)
    else:
        cars = Car.objects.all()
    return render(request, 'cars/car_list.html', {'cars': cars})

def car_detail_view(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'cars/car_detail.html', {'car': car})

@login_required # This ensures only logged-in users can access this page
def list_car_view(request):
    if request.method == 'POST':
        # Create a form instance with the submitted data and files
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the new car to the database
            form.save()
            messages.success(request, 'Your car has been listed successfully!')
            return redirect('car_list') # Redirect to the car list page
    else:
        # If it's a GET request, create an empty form
        form = CarForm()
        
    return render(request, 'cars/list_car.html', {'form': form})

