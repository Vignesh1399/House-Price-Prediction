from django import forms
from home.models import House
from django.core.validators import DecimalValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_int(value):
    if not(isinstance(value, int)):
        raise ValidationError(
            _('%(value)s is not an Integer'),
            params={'value': value},
        )

class DateInput(forms.DateInput):
	input_type = 'date'
	
class HouseForm(forms.ModelForm):
	transaction_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), label = 'Transaction Date', help_text = 'Date on 	which the house would be sold')
	age = forms.DecimalField(decimal_places=1, label = 'Age', help_text = 'Age of Your House (In years)', 
	validators = [DecimalValidator(decimal_places = 1, max_digits = 10)])
	mrt_station = forms.DecimalField(decimal_places=5, label = 'MRT Distance', help_text = 'Distance to nearest MRT Station (In Km)', 
	validators = 	[DecimalValidator(decimal_places = 5, max_digits = 10)])
	convenience_stores = forms.IntegerField(label = 'Convenience Stores', help_text = 'Distance to nearest Convenience Store as an Integer (in  	Km)', validators = [validate_int])
	latitude = forms.DecimalField(decimal_places=5, label = 'Latitude', help_text = 'Please Use Google Maps to find Latitude',
	validators = [DecimalValidator(decimal_places = 5, max_digits = 10)])
	longitude = forms.DecimalField(decimal_places=5, label = 'Longitude', help_text = 'Please Use Google Maps to find Longitude',
	validators = [DecimalValidator(decimal_places = 5, max_digits = 10)])
	
	class Meta:
		model = House
		fields = ('transaction_date', )
