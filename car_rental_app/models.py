from django.db import models

# Create your models here.
class Car(models.Model):
    car_id = models.IntegerField(primary_key=True)
    model = models.CharField(max_length=45, null=True)
    brand = models.CharField(max_length=45, null=True)
    color = models.CharField(max_length=45, null=True)
    description = models.CharField(max_length=500, null=True)
    date_of_purchase = models.DateTimeField('Date of purchase', null=True)
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

