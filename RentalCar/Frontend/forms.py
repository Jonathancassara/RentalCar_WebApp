from django import forms
from .models import Rental

# Form to add a rental
class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['car', 'driver', 'comments']

# Form to update a rental
class RentalUpdateForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['return_date', 'comments']
