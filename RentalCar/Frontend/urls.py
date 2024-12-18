from django.urls import path
from .views import index, list_rentals, add_rental, update_rental, delete_rental, drivers,list_drivers, delete_drivers, add_driver, rentals, cars, add_car, list_cars, delete_cars

urlpatterns = [
    path('', index, name='index'),  # Home Page
    path('list/', list_rentals, name='list_rentals'),  # List Rentals
    path('add/', add_rental, name='add_rental'),  # Add Rental
    path('update/<int:pk>/', update_rental, name='update_rental'),  # Update Rental
    path('delete/<int:pk>/', delete_rental, name='delete_rental'),  # Delete Rental
    path('drivers/', drivers, name='drivers'),# Drivers Page
    path('drivers/add/', add_driver, name='add_driver'), #Add Drivers
    path('list_drivers/', list_drivers, name='list_drivers'), #list Drivers
    path('drivers/delete/', delete_drivers, name='delete_drivers'),  #delete drivers 
    path('rentals/', rentals, name='rentals'),  # Rentals Page
    #path('cars/', cars, name='cars'),          # Cars Page
    path('cars/add/', add_car, name='add_car'),
    path('cars/', list_cars, name='list_cars'),
    path('cars/delete/', delete_cars, name='delete_cars'),

]
