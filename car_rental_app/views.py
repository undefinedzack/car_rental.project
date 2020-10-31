from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.decorators.http import require_POST

from .models import Customer, Car, Booking
from .forms import Query_Form, Car_Form, id_form, Car_update_form, Customer_form, Booking_form

import datetime


def home(request):
    query_form = Query_Form()

    context = {
        'query_form': query_form
    }

    return render(request, 'car_rental_app/home.html', context)


def car(request):
    cars = Car.objects.all()
    car_form = Car_Form()
    car_id_form = id_form()

    color_set = set(str(colors.color) for colors in Car.objects.all() if str(colors.color) != '')
    print(color_set)

    context = {
        'cars': cars,
        'car_form': car_form,
        'car_id_form': car_id_form,
        'color_set': color_set
    }

    return render(request, 'car_rental_app/car.html', context)


def customer(request):
    customers = Customer.objects.all()
    customer_form = Customer_form()
    customer_id_form = id_form()

    context = {
        'customers': customers,
        'customer_form': customer_form,
        'customer_id_form': customer_id_form
    }

    return render(request, 'car_rental_app/customers.html', context)


def booking(request):
    bookings = Booking.objects.all()
    booking_form = Booking_form()
    booking_id_form = id_form()

    context = {
        'bookings': bookings,
        'booking_form': booking_form,
        'booking_id_form': booking_id_form
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
            if l[0].lower() == 'car':
                queried = Car.objects.all()

        if len(l) > 1:
            if l[0].lower() == 'car':
                queried = Car.objects.filter(color__iexact=l[1].lower())
                print(queried)

    context = {
        'queried': queried
    }

    return render(request, 'car_rental_app/result.html', context)


# CAR SECTION
@require_POST
def add_car(request):
    car_form = Car_Form(request.POST)

    # if car_form.is_valid():
    avaibility = str(request.POST['available'])
    new_car = Car(
        model=request.POST['model'],
        brand=request.POST['brand'],
        color=request.POST['color'],
        description=request.POST['description'],
        date_of_purchase=request.POST['date_of_purchase'],
        # time_of_purchase=request.POST['time_of_purchase'],
        available=True if avaibility == 'on' else False

    )
    new_car.save()

    return redirect('car_rental_app:cars')


def delete_car(request, id):
    car = Car.objects.get(pk=id)

    car.delete()

    return redirect('car_rental_app:cars')


@require_POST
def delete_car_user_input(request):
    idz = int(request.POST['idz'])
    car = Car.objects.get(pk=idz)

    car.delete()

    return redirect('car_rental_app:cars')


def update_car(request, id):
    car = Car.objects.get(pk=id)

    edit_form = Car_update_form(instance=car)

    if request.method == 'POST':
        edit_form = Car_update_form(request.POST, instance=car)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('car_rental_app:cars')

    context = {
        'edit_form': edit_form,
        'key': id
    }

    return render(request, 'car_rental_app/car_update.html', context)


@require_POST
def update_car_user_input(request):
    # bug update via update_car_user gets created with new thing not updating present one to update
    # if request.method == 'POST':
    #     edit_form = Car_update_form(request.POST)
    #     if edit_form.is_valid():
    #         edit_form.save()
    #         return redirect('car_rental_app:cars')

    idz = int(request.POST['idz'])
    car = Car.objects.get(pk=idz)

    edit_form = Car_update_form(instance=car)

    context = {
        'edit_form': edit_form,
        'key': idz
    }

    return render(request, 'car_rental_app/car_update.html', context)


# CUSTOMER SECTION
@require_POST
def add_customer(request):
    customer_form = Customer_form(request.POST)

    if customer_form.is_valid():
        customer_form.save()

    return redirect('car_rental_app:customers')


def delete_customer(request, id):
    customer = Customer.objects.get(pk=id)

    customer.delete()

    return redirect('car_rental_app:customers')


@require_POST
def delete_customer_user_input(request):
    idz = int(request.POST['idz'])
    customer = Customer.objects.get(pk=idz)

    customer.delete()

    return redirect('car_rental_app:customers')


def update_customer(request, id):
    present_customer = Customer.objects.get(pk=id)

    edit_form = Customer_form(instance=present_customer)

    if request.method == 'POST':
        edit_form = Customer_form(request.POST, instance=present_customer)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('car_rental_app:customers')

    context = {
        'edit_form': edit_form,
        'key': id
    }

    return render(request, 'car_rental_app/customer_update.html', context)


def update_customer_by_user(request):
    idz = int(request.POST['idz'])
    customer = Customer.objects.get(pk=idz)

    edit_form = Customer_form(instance=customer)

    context = {
        'edit_form': edit_form,
        'key': idz
    }

    return render(request, 'car_rental_app/customer_update.html', context)


# BOOKING SECTION

@require_POST
def add_booking(request):
    booking_form = Booking_form(request.POST)
    if booking_form.is_valid():
        booking_form.save()

    return redirect('car_rental_app:bookings')


def delete_booking(request, id):
    booking = Booking.objects.get(pk=id)

    booking.delete()

    return redirect('car_rental_app:bookings')


@require_POST
def delete_booking_user_input(request):
    idz = int(request.POST['idz'])
    booking = Booking.objects.get(pk=idz)

    booking.delete()

    return redirect('car_rental_app:bookings')


def update_booking(request, id):
    present_booking = Booking.objects.get(pk=id)

    edit_form = Booking_form(instance=present_booking)

    if request.method == 'POST':
        edit_form = Booking_form(request.POST, instance=present_booking)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('car_rental_app:bookings')

    context = {
        'edit_form': edit_form,
        'key': id
    }

    return render(request, 'car_rental_app/booking_update.html', context)


def update_booking_by_user(request):
    idz = int(request.POST['idz'])
    present_booking = Booking.objects.get(pk=idz)

    edit_form = Booking_form(instance=present_booking)

    context = {
        'edit_form': edit_form,
        'key': idz
    }

    return render(request, 'car_rental_app/booking_update.html', context)


class ChartView(TemplateView):
    template_name = 'car_rental_app/charts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        carzzz = []
        namezzz = []
        for x in range(1999, 2021):
            carzzz.append(Car.objects.filter(date_of_purchase__year=x).count())
            namezzz.append(f'{x}')

        max_car_sales_year = int(namezzz[carzzz.index(max(carzzz))])
        min_car_sales_year = int(namezzz[carzzz.index(min(carzzz))])

        context = {
            'namezzz': namezzz,
            'carzzz': carzzz,
            'max_car_sales_year': max_car_sales_year,
            'min_car_sales_year': min_car_sales_year
        }

        return context


def good_cars(request):
    in_good_condition = [good_one for good_one in Car.objects.filter(description__iexact='good')]

    context = {
        'in_good_condition': in_good_condition,
    }

    return render(request, 'car_rental_app/goodones.html', context)


def fair_cars(request):
    in_fair_condition = [good_one for good_one in Car.objects.filter(description__iexact='fair')]

    context = {
        'in_fair_condition': in_fair_condition,
    }

    return render(request, 'car_rental_app/fair_cars.html', context)


def excellent_cars(request):
    in_excellent_condition = [good_one for good_one in Car.objects.filter(description__iexact='excellent')]

    context = {
        'in_excellent_condition': in_excellent_condition,
    }

    return render(request, 'car_rental_app/excellent_cars.html', context)


def color_of_car(request, color):
    colorzzz = [good_one for good_one in Car.objects.filter(color__iexact=color)]
    color_set = set([colors.color for colors in Car.objects.all()])

    context = {
        'colorzzz': colorzzz,
        'color_set': color_set
    }

    return render(request, 'car_rental_app/car_color.html', context)


def cars_after_date(request):
    after_date = [x for x in
                  Car.objects.filter(date_of_purchase__gt=datetime.date(2010, 1, 1)).order_by('date_of_purchase')]

    context = {
        'after_date': after_date
    }

    return render()
