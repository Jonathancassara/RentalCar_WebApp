from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Car, Driver, Rental
import json
from django.utils.html import escape

# ------------------------- Home Page ------------------------- #
def index(request):
    """
    Renders the home page.
    """
    return render(request, 'index.html')

# ------------------------- Rentals ------------------------- #
def rentals(request):
    """
    Renders the Rentals management page.
    """
    return render(request, 'rentals.html')

def list_rentals(request):
    """
    Renders the rental list page with all rentals.
    """
    rentals = Rental.objects.select_related('car', 'driver')
    return render(request, 'list_rentals.html', {'rentals': rentals})

def add_rental(request):
    """
    Adds a new rental with validation and a confirmation modal.
    """
    if request.method == 'POST':
        data = json.loads(request.body)
        car_id = data.get('car_id')
        driver_id = data.get('driver_id')
        rent_date = data.get('rent_date')
        comments = escape(data.get('comments', '')[:500])  # Escape input and limit to DB max length

        Rental.objects.create(
            car_id=car_id,
            driver_id=driver_id,
            rent_date=rent_date,
            comments=comments
        )
        return JsonResponse({'success': True})

    # Get drivers and available cars for the form
    drivers = Driver.objects.all()
    rented_car_ids = Rental.objects.filter(return_date__isnull=True).values_list('car_id', flat=True)
    available_cars = Car.objects.exclude(id__in=rented_car_ids)

    return render(request, 'add_rental.html', {
        'drivers': drivers,
        'available_cars': available_cars
    })

def update_rental(request, pk):
    """
    Updates a rental record.
    """
    rental = get_object_or_404(Rental, pk=pk)
    if request.method == 'POST':
        rental.car_id = request.POST.get('car_id')
        rental.driver_id = request.POST.get('driver_id')
        rental.rent_date = request.POST.get('rent_date')
        rental.return_date = request.POST.get('return_date')
        rental.comments = request.POST.get('comments', '')
        rental.save()
        return redirect('list_rentals')
    return render(request, 'update_rental.html', {'rental': rental})

def delete_rental(request, pk):
    """
    Deletes a rental record.
    """
    rental = get_object_or_404(Rental, pk=pk)
    rental.delete()
    return redirect('list_rentals')

# ------------------------- Drivers ------------------------- #
def drivers(request):
    """
    Renders the drivers management page.
    """
    return render(request, 'drivers.html')

def list_drivers(request):
    """
    Displays a list of drivers.
    """
    drivers = Driver.objects.all()
    return render(request, 'list_drivers.html', {'drivers': drivers})

def add_driver(request):
    """
    Adds a new driver with validation for required fields.
    """
    if request.method == 'POST':
        # Parse data from the request
        data = json.loads(request.body)
        name = data.get('name', '').strip()
        surname = data.get('surname', '').strip()
        email = data.get('email', '').strip()
        phone_number = data.get('phone_number', '').strip()

        # Validate required fields
        if not name or not surname or not email or not phone_number:
            return JsonResponse({'success': False, 'error': 'All fields are required!'}, status=400)

        # Escape inputs to prevent XSS
        name = escape(name)
        surname = escape(surname)
        email = escape(email)
        phone_number = escape(phone_number)

        # Save the driver to the database
        Driver.objects.create(
            name=name,
            surname=surname,
            email=email,
            phone_number=phone_number
        )

        return JsonResponse({'success': True})

    return render(request, 'add_driver.html')

def delete_drivers(request):
    """
    Deletes selected drivers based on IDs sent via JSON.
    """
    if request.method == 'POST':
        data = json.loads(request.body)
        ids = data.get('ids', [])
        Driver.objects.filter(id__in=ids).delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=405)

# ------------------------- Cars ------------------------- #
def cars(request):
    """
    Renders the cars management page.
    """
    return render(request, 'cars.html')

# List Cars View
def list_cars(request):
    """
    Displays all cars in a simple table without delete functionality.
    """
    cars = Car.objects.all()
    return render(request, 'list_cars.html', {'cars': cars})

def add_car(request):
    """
    Adds a new car with a POST request.
    """
    if request.method == 'POST':
        make = request.POST.get('make')
        model = request.POST.get('model')
        registration_number = request.POST.get('registration_number')

        Car.objects.create(
            make=make,
            model=model,
            registration_number=registration_number
        )
        return JsonResponse({'success': True})
    return render(request, 'add_car.html')

# Remove Cars View
def remove_cars(request):
    """
    Displays cars with checkboxes and a delete button for removing cars.
    """
    cars = Car.objects.all()
    return render(request, 'remove_cars.html', {'cars': cars})

# Delete Cars API
def delete_cars(request):
    """
    Deletes selected cars based on IDs sent via JSON.
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            ids = data.get('ids', [])
            Car.objects.filter(id__in=ids).delete()
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
    return JsonResponse({'success': False}, status=405)