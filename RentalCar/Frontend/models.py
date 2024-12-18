from django.db import models

# Drivers Table
class Driver(models.Model):
    id = models.AutoField(primary_key=True)  # Clé primaire, auto-incrémentée
    name = models.CharField(max_length=50, null=False)  # Not null
    surname = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=100, null=False)
    phone_number = models.CharField(max_length=50, null=False)

    def __str__(self):
        return f"{self.name} {self.surname}"

# Cars Table
class Car(models.Model):
    id = models.AutoField(primary_key=True)  # Clé primaire, auto-incrémentée
    make = models.CharField(max_length=50, null=False)  # Not null
    model = models.CharField(max_length=100, null=False)
    registration_number = models.CharField(max_length=10, unique=True, null=False)  # Unique, not null

    def __str__(self):
        return f"{self.make} {self.model} - {self.registration_number}"

# Rentals Table
class Rental(models.Model):
    id = models.AutoField(primary_key=True)  # Clé primaire, auto-incrémentée
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=False, related_name="rentals")  # Clé étrangère vers Car
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=False, related_name="rentals")  # Clé étrangère vers Driver
    rent_date = models.DateTimeField(null=False, auto_now_add=True)  # Date par défaut à l'heure actuelle
    return_date = models.DateTimeField(null=True, blank=True)  # Peut être vide
    comments = models.TextField(null=True, blank=True)  # Champ facultatif pour les commentaires

    def __str__(self):
        return f"Rental: {self.car} by {self.driver}"
