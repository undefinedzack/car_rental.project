from django.urls import path

from . import views

app_name = 'car_rental_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name= 'search'),
    path('cars/', views.car, name= 'cars'),
    path('cars/add_car/', views.add_car, name='add car'),

    path('customers/', views.customer, name='customers'),
    path('bookings/', views.booking, name='bookings')
]