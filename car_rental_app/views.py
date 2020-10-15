from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Customer, Car
from .forms import Query_Form

def home(request):

    query_form = Query_Form()


    context = {
        'query_form' : query_form
    }

    return render(request, 'car_rental_app/home.html', context)

@require_POST
def search(request):

    query_form = Query_Form(request.POST)
    cars = Car.objects.all()
    customers = Customer.objects.all()

    if query_form.is_valid():
        text = request.POST['text']

        l = list(text.split(' '))

        if len(l) == 1:
            if (l[0].lower() == 'car'):
                queried = Car.objects.all()

        if len(l) > 1:
            if (l[0].lower() == 'car' ):
                queried = Car.objects.filter(color__iexact=l[1].lower())
                print(queried)

    context = {
        'queried': queried
    }

    return render(request, 'car_rental_app/result.html', context)

