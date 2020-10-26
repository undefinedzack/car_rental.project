from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Customer, Car, Booking
from .forms import Query_Form, Car_Form

def home(request):

    query_form = Query_Form()


    context = {
        'query_form' : query_form
    }

    return render(request, 'car_rental_app/home.html', context)

def car(request):
    cars = Car.objects.all()
    car_form = Car_Form()

    context = {
        'cars' : cars,
        'car_form' : car_form,
    }

    return render(request, 'car_rental_app/car.html', context)

def customer(request):
    customers = Customer.objects.all()

    context = {
        'customers' : customers
    }

    return render(request, 'car_rental_app/customers.html', context)

def booking(request):
    bookings = Booking.objects.all()

    context = {
        'bookings' : bookings
    }

    return render(request, 'car_rental_app/bookings.html', context)

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

@require_POST
def add_car(request):
    car_form = Car_Form(request.POST)

    # if car_form.is_valid():
    new_car = Car(
        model=request.POST['model'],
        brand=request.POST['brand'],
        color=request.POST['color'],
        description=request.POST['description'],
        date_of_purchase=request.POST['date_of_purchase'],
        time_of_purchase=request.POST['time_of_purchase'],
        #available=request.POST['available']

    )
    new_car.save()

    return redirect('car_rental_app:cars')





