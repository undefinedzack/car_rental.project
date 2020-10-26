from django.db import models


class Car(models.Model):
    car_id = models.IntegerField(primary_key=True)
    model = models.CharField(max_length=45, null=True)
    brand = models.CharField(max_length=45, null=True)
    color = models.CharField(max_length=45, null=True)
    description = models.CharField(max_length=500, null=True)
    date_of_purchase = models.DateField('Date of purchase', null=True)
    time_of_purchase = models.TimeField('Time of purchase', null=True)
    available = models.BooleanField(default=False)

    def __str__(self):
        return self.brand


class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=45, null=True)
    last_name = models.CharField(max_length=45, null=True)
    mobile_no = models.BigIntegerField()
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name


class Booking(models.Model):
    booking_id = models.IntegerField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_of_issue = models.DateTimeField('Date of Issue')
    date_of_return = models.DateTimeField('Date of Return')
    amount = models.IntegerField
    pickup_location = models.CharField(max_length=500)

    def __str__(self):
        return str(self.booking_id)
