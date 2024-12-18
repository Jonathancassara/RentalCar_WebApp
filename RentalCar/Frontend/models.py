from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=50)  # Manufacturer of the car
    model = models.CharField(max_length=100)  # Car model
    registration_number = models.CharField(max_length=10)  # Registration plate

    def __str__(self):
        return f"{self.make} {self.model} ({self.registration_number})"


class Driver(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Rental(models.Model):
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    driver = models.ForeignKey('Driver', on_delete=models.CASCADE)
    rent_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    comments = models.TextField(max_length=500, blank=True)  # Comment field

    def __str__(self):
        return f"{self.driver} rented {self.car} on {self.rent_date}"
