from django.contrib import admin

from .models import Car,Customer, Booking

admin.site.register(Car)
admin.site.register(Customer)
admin.site.register(Booking)