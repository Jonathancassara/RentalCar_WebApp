from django.urls import path
from .views import (
    index, rentals, list_rentals, add_rental, update_rental, delete_rental,
    drivers, list_drivers, add_driver, delete_drivers,
    cars, list_cars, add_car, delete_cars, remove_cars
)

urlpatterns = [
    path('', index, name='index'),

    # Rentals
    path('rentals/', rentals, name='rentals'),
    #path('rentals/', list_rentals, name='list_rentals'),
    path('rentals/add/', add_rental, name='add_rental'),
    path('rentals/update/<int:pk>/', update_rental, name='update_rental'),
    path('rentals/delete/<int:pk>/', delete_rental, name='delete_rental'),

    # Drivers
    path('drivers/', drivers, name='drivers'),
    path('drivers/list/', list_drivers, name='list_drivers'),
    path('drivers/add/', add_driver, name='add_driver'),
    path('drivers/delete/', delete_drivers, name='delete_drivers'),

    # Cars
    path('cars/', cars, name='cars'),
    path('cars/list/', list_cars, name='list_cars'),  # Page to list cars
    path('cars/add/', add_car, name='add_car'),
    path('cars/remove/', remove_cars, name='remove_cars'),  # Page to remove cars
    path('cars/delete/', delete_cars, name='delete_cars'),  # API endpoint for deleting cars
]
