from django.shortcuts import render, redirect, get_object_or_404
from .models import Rental, Driver, Car
from .forms import RentalForm, RentalUpdateForm
from django.http import JsonResponse
import json

# View: Home Page
def index(request):
    return render(request, 'index.html')

# View: List of Rentals
def list_rentals(request):
    rentals = Rental.objects.all()
    return render(request, 'list_rentals.html', {'rentals': rentals})

# View: Add a New Rental
def add_rental(request):
    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_rentals')
    else:
        form = RentalForm()
    return render(request, 'add_rental.html', {'form': form})

# View: Update a Rental
def update_rental(request, pk):
    rental = get_object_or_404(Rental, pk=pk)
    if request.method == 'POST':
        form = RentalUpdateForm(request.POST, instance=rental)
        if form.is_valid():
            form.save()
            return redirect('list_rentals')
    else:
        form = RentalUpdateForm(instance=rental)
    return render(request, 'update_rental.html', {'form': form, 'rental': rental})

# View: Delete a Rental
def delete_rental(request, pk):
    rental = get_object_or_404(Rental, pk=pk)
    if request.method == 'POST':
        rental.delete()
        return redirect('list_rentals')
    return render(request, 'delete_rental.html', {'rental': rental})

# View: Home Page
def index(request):
    return render(request, 'index.html')

# View: Drivers Page
def drivers(request):
    return render(request, 'drivers.html')

def add_driver(request):
    if request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        phone = request.POST['phone']

        # Create and save the new driver
        Driver.objects.create(name=name, surname=surname, email=email, phone_number=phone)
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)

# View to list all drivers
def list_drivers(request):
    drivers = Driver.objects.all()
    return render(request, 'list_drivers.html', {'drivers': drivers})

# View to delete selected drivers
def delete_drivers(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            ids = data.get('ids', [])
            Driver.objects.filter(id__in=ids).delete()
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)

# View: Rentals Page
def rentals(request):
    return render(request, 'rentals.html')

# View: Cars Page
def cars(request):
    return render(request, 'cars.html')

def add_car(request):
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

def list_cars(request):
    cars = Car.objects.all()
    return render(request, 'list_cars.html', {'cars': cars})

def delete_cars(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        ids = data.get('ids', [])
        Car.objects.filter(id__in=ids).delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=405)