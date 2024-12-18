from django.urls import path
from .views import index, list_rentals, add_rental, update_rental, delete_rental

urlpatterns = [
    path('', index, name='index'),  # Home Page
    path('list/', list_rentals, name='list_rentals'),  # List Rentals
    path('add/', add_rental, name='add_rental'),  # Add Rental
    path('update/<int:pk>/', update_rental, name='update_rental'),  # Update Rental
    path('delete/<int:pk>/', delete_rental, name='delete_rental'),  # Delete Rental
]
