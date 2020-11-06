# Generated by Django 3.0.5 on 2020-11-05 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=45)),
                ('brand', models.CharField(max_length=45)),
                ('color', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=500)),
                ('date_of_purchase', models.DateField(verbose_name='Date of purchase')),
                ('available', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('mobile_no', models.BigIntegerField()),
                ('car_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_rental_app.Car')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_issue', models.DateField(verbose_name='Date of Issue')),
                ('date_of_return', models.DateField(verbose_name='Date of Return')),
                ('amount', models.IntegerField()),
                ('pickup_location', models.CharField(max_length=500)),
                ('car_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_rental_app.Car')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_rental_app.Customer')),
            ],
        ),
    ]
