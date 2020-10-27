from django import forms

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

class Car_id_form(forms.Form):
    idz = forms.IntegerField()

