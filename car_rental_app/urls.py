from django.urls import path

from . import views

app_name = 'car_rental_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),

    path('cars/', views.car, name='cars'),
    path('cars/add_car/', views.add_car, name='add car'),
    path('cars/delete_car/<int:id>', views.delete_car, name='delete car'),
    path('cars/delete_car_user_input', views.delete_car_user_input, name='delete car by user'),
    path('cars/update_car/<int:id>', views.update_car, name='update car'),
    path('cars/update_car_user_input', views.update_car_user_input, name='update car by user'),

    path('customers/', views.customer, name='customers'),
    path('customers/add_customer', views.add_customer, name='add customer'),
    path('customer/delete_customer/<int:id>', views.delete_customer, name='delete customer'),
    path('customer/delete_customer_user_input', views.delete_customer_user_input, name='delete customer user input'),
    path('customer/update_customer/<int:id>', views.update_customer, name='update customer'),
    path('customer/update_customer_user_input', views.update_customer_by_user, name='update customer by user'),

    path('bookings/', views.booking, name='bookings'),
    path('bookings/add_booking', views.add_booking, name='add booking'),
    path('bookings/delete_booking/<int:id>', views.delete_booking, name='delete booking'),
    path('bookings/delete_booking_user_input', views.delete_booking_user_input, name='delete booking user input'),
    path('bookings/update_booking/<int:id>', views.update_booking, name='update booking'),
    path('bookings/update_booking_user_input', views.update_booking_by_user, name='update booking by user'),

    #QUERIES SECTION
    path('cars/charts', views.ChartView.as_view(), name='chart'),
    path('cars/goodones', views.good_cars, name='good cars'),
    path('cars/fairones', views.fair_cars, name='fair cars'),
    path('cars/excellentones', views.excellent_cars, name='excellent cars'),
    path('cars/car_in_range', views.cars_date_query, name='car in range'),
    path('cars/color/<str:color>', views.color_of_car, name='car color'),

    path('customers/customer_charts', views.customer_queried_by_cars, name='Chart Customer'),
    path('customers/find_customer_by_name', views.find_customer_with_name, name='find customer by name')


]
