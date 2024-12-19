from django.db import models
from django.utils.timezone import now


class Driver(models.Model):
    """
    Driver model stores driver information.
    """
    name = models.CharField(max_length=50, null=False)  # First Name, required
    surname = models.CharField(max_length=50, null=False)  # Last Name, required
    email = models.EmailField(max_length=100, null=False)  # Email, required
    phone_number = models.CharField(max_length=50, null=False)  # Phone Number, required

    def __str__(self):
        return f"{self.name} {self.surname}"


class Car(models.Model):
    """
    Car model stores car details.
    """
    make = models.CharField(max_length=50, null=False)  # Car make, required
    model = models.CharField(max_length=100, null=False)  # Car model, required
    registration_number = models.CharField(max_length=10, null=False, unique=True)  # Registration Number, required

    def __str__(self):
        return f"{self.make} {self.model} ({self.registration_number})"


class Rental(models.Model):
    """
    Rental model stores rental transactions.
    """
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="rentals")  # Foreign key to Car, not null
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name="rentals")  # Foreign key to Driver, not null
    rent_date = models.DateTimeField(null=False, default=now)  # Rent Date and Time, default is current time
    return_date = models.DateTimeField(null=True, blank=True)  # Optional Return Date and Time
    comments = models.TextField(null=True, blank=True)  # Optional comments

    def __str__(self):
        return f"Rental: {self.driver} - {self.car} on {self.rent_date}"
