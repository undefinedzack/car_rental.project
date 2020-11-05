from django.db import models


class Car(models.Model):
    model = models.CharField(max_length=45)
    brand = models.CharField(max_length=45)
    color = models.CharField(max_length=45)
    description = models.CharField(max_length=500)
    date_of_purchase = models.DateField('Date of purchase')
    #time_of_purchase = models.TimeField('Time of purchase')
    available = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} {self.model} {self.brand}"


class Customer(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    mobile_no = models.BigIntegerField()
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name


class Booking(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_of_issue = models.DateField('Date of Issue')
    date_of_return = models.DateField('Date of Return')
    amount = models.IntegerField()
    pickup_location = models.CharField(max_length=500)

