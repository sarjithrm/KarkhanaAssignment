# Generated by Django 3.2.3 on 2021-05-21 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipt', '0002_tollreceipt_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tollreceipt',
            name='journey_type',
            field=models.CharField(choices=[('Single', 'Single Journey'), ('Return', 'Return Journey')], default='Single', max_length=6),
        ),
        migrations.AlterField(
            model_name='tollreceipt',
            name='vehicle_type',
            field=models.CharField(choices=[('Car', 'Car/Jeep'), ('Bus', 'Buses'), ('Truck', 'Trucks')], default='Car', max_length=5),
        ),
    ]
