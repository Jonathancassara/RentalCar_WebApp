from django.urls import path
from .views import (
    index, 
    list_rentals, add_rental, update_rental, delete_rental,
    drivers, add_driver, list_drivers, delete_drivers, 
    rentals, 
    add_car, list_cars, delete_cars
)

urlpatterns = [
    # Home Page
    path('', index, name='index'),

    # Rentals
    path('rentals/', rentals, name='rentals'),
    path('rentals/list/', list_rentals, name='list_rentals'),
    path('rentals/add/', add_rental, name='add_rental'),
    path('rentals/update/<int:pk>/', update_rental, name='update_rental'),
    path('rentals/delete/<int:pk>/', delete_rental, name='delete_rental'),

    # Drivers
    path('drivers/', drivers, name='drivers'),
    path('drivers/add/', add_driver, name='add_driver'),
    path('drivers/list/', list_drivers, name='list_drivers'),
    path('drivers/delete/', delete_drivers, name='delete_drivers'),

    # Cars
    path('cars/', list_cars, name='list_cars'),
    path('cars/add/', add_car, name='add_car'),
    path('cars/delete/', delete_cars, name='delete_cars'),
]
