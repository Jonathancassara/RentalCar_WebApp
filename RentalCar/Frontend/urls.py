from django.urls import path
from .views import (
    index, rentals, list_rentals, add_rental, update_rental, delete_rental,modify_rental,finish_rental,
    drivers, list_drivers, add_driver, modify_driver, delete_drivers,
    cars, list_cars, add_car, delete_cars, remove_cars
)

urlpatterns = [
    path('', index, name='index'),

    # Rentals
    path('rentals/', rentals, name='rentals'),
    #path('rentals/', list_rentals, name='list_rentals'),
    path('rentals/add/', add_rental, name='add_rental'),  # Add Rental Page
    path('rentals/update/<int:pk>/', update_rental, name='update_rental'),
    path('rentals/delete/<int:pk>/', delete_rental, name='delete_rental'),
    path('rentals/modify/', modify_rental, name='modify_rental'),  # Modify Rental
    path('rentals/finish/', finish_rental, name='finish_rental'),  # Finish Rental
    path('rentals/list/', list_rentals, name='list_rentals'),  # List Rentals

    # Drivers
    path('drivers/', drivers, name='drivers'),
    path('drivers/add/', add_driver, name='add_driver'),  # Add Driver Page
    path('drivers/list/', list_drivers, name='list_drivers'),  # List Drivers Page
    path('drivers/modify/<int:driver_id>/', modify_driver, name='modify_driver'), # Modify Drivers Page
    path('drivers/delete/', delete_drivers, name='delete_drivers'),  # Delete Drivers
    path('drivers/remove/', delete_drivers, name='delete_drivers'),  # Remove Drivers Page

    # Cars
    path('cars/', cars, name='cars'),
    path('cars/list/', list_cars, name='list_cars'),  # Page to list cars
    path('cars/add/', add_car, name='add_car'),
    path('cars/remove/', remove_cars, name='remove_cars'),  # Page to remove cars
    path('cars/delete/', delete_cars, name='delete_cars'),  # API endpoint for deleting cars
]
