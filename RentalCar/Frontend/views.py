from django.shortcuts import render, redirect, get_object_or_404
from .models import Rental, Driver, Car
from .forms import RentalForm, RentalUpdateForm

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
