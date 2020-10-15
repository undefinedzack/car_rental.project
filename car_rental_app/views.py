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

    if query_form.is_valid():
        text = request.POST['text']

        l = list(text.split(' '))

        if (l[0].lower() == 'car'):
            print(Car.objects.all())

    context = {}

    return redirect('car_rental_app:home')

