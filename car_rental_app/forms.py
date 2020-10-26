from django import forms

class Query_Form(forms.Form):
    text = forms.CharField(max_length=1000,
                           widget= forms.TextInput(
                               attrs={ 'class' : 'form-control',
                                       'aria-label': 'Query',
                                       'aria-describedby' : 'inputGroup-sizing-default',
                                       'placeholder' : 'Query?'}
                           ))

class Car_Form(forms.Form):
    model = forms.CharField(max_length=45,
                            widget=forms.TextInput(
                                attrs={'class': 'form-control',
                                       'aria-label': 'Model',
                                       'aria-describedby': 'inputGroup-sizing-default',
                                       'placeholder': 'Car Model?'}
                            ))
    brand = forms.CharField(max_length=45,
                            widget=forms.TextInput(
                                attrs={'class': 'form-control',
                                       'aria-label': 'Brand',
                                       'aria-describedby': 'inputGroup-sizing-default',
                                       'placeholder': 'Car Brand?'}
                            ))
    color = forms.CharField(max_length=45,
                            widget=forms.TextInput(
                                attrs={'class': 'form-control',
                                       'aria-label': 'Color',
                                       'aria-describedby': 'inputGroup-sizing-default',
                                       'placeholder': 'Car Color?'}
                            ))
    description = forms.CharField(max_length=500,
                                  widget=forms.TextInput(
                                      attrs={'class': 'form-control',
                                             'aria-label': 'Description',
                                             'aria-describedby': 'inputGroup-sizing-default',
                                             'placeholder': 'Description?'}
                                  ))
    # date_of_purchase = forms.DateTimeField(
    #                              widget=forms.DateTimeInput(
    #                                   attrs={'class': 'form-control',
    #                                          'aria-label': 'Date & Time',
    #                                          'aria-describedby': 'inputGroup-sizing-default',
    #                                          'placeholder': 'Date and Time?'}
    #                               ))
    available = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={'class': 'form-control',
                   'aria-label': 'Date & Time',
                   'aria-describedby': 'inputGroup-sizing-default',
                   'placeholder': 'Date and Time?'}
        ))

