from django import forms

from .models import Car, Customer, Booking

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class Query_Form(forms.Form):
    text = forms.CharField(max_length=1000)

class Car_Form(forms.Form):
    model = forms.CharField()
    brand = forms.CharField()
    color = forms.CharField()
    description = forms.CharField()
    date_of_purchase = forms.DateField(widget=DateInput)
    time_of_purchase = forms.TimeField(widget=TimeInput)
    available = forms.BooleanField()

class id_form(forms.Form):
    idz = forms.IntegerField()

class Car_update_form(forms.ModelForm):

    class Meta:
        model = Car
        fields = '__all__'

class Customer_form(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'

class Booking_form(forms.ModelForm):

    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'date_of_issue' : DateInput,
            'date_of_return' : DateInput
        }
