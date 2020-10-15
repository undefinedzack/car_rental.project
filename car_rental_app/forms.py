from django import forms

class Query_Form(forms.Form):
    text = forms.CharField(max_length=1000,
                           widget= forms.TextInput(
                               attrs={ 'class' : 'form-control',
                                       'aria-label': 'Query',
                                       'aria-describedby' : 'inputGroup-sizing-default',
                                       'placeholder' : 'Query?'}
                           ))