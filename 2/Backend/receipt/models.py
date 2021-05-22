from django.db import models
from datetime import datetime

class TollReceipt(models.Model):
    ONE_WAY = 'Single'
    TWO_WAY = 'Return'
    JOURNEY_TYPE_CHOICES = [
        (ONE_WAY, 'Single Journey'),
        (TWO_WAY, 'Return Journey'),
    ]

    CAR = 'Car'
    BUS = 'Bus'
    TRUCK = 'Truck'
    VEHICLE_TYPE_CHOICES = [
        (CAR, 'Car/Jeep'),
        (BUS, 'Buses'),
        (TRUCK, 'Trucks')
    ]

    ONE_HUNDRED = 100
    TWO_HUNDRED = 200
    PRICE_CHOICES = [
        (ONE_HUNDRED, 100),
        (TWO_HUNDRED, 200)
    ]

    receipt_id = models.AutoField(primary_key=True)
    vehicle_number = models.CharField(max_length=10)
    journey_type = models.CharField(max_length=6, choices=JOURNEY_TYPE_CHOICES, default=ONE_WAY)
    vehicle_type = models.CharField(max_length=5, choices=VEHICLE_TYPE_CHOICES, default=CAR)
    journey_date_time = models.DateTimeField(auto_now_add=True)
    journey_status = models.CharField(max_length=10)
    journey_towards = models.CharField(max_length=255)
    price = models.IntegerField(choices=PRICE_CHOICES, default=ONE_HUNDRED)

    def get_receipt_id(self):
        return self.receipt_id

    def set_receipt_id(self, receipt_id):
        self.receipt_id = receipt_id

    def get_vehicle_number(self):
        return self.vehicle_number

    def set_vehicle_number(self, vehicle_number):
        self.vehicle_number = vehicle_number

    def get_journey_type(self):
        return self.journey_type

    def set_journey_type(self, journey_type):
        self.journey_type = journey_type

    def get_vehicle_type(self):
        return self.vehicle_type

    def set_vehicle_type(self, vehicle_type):
        self.vehicle_type = vehicle_type

    def get_journey_date_time(self):
        return self.journey_date_time

    def get_journey_status(self):
        return self.journey_status

    def set_journey_status(self, journey_status):
        self.journey_status = journey_status

    def get_journey_towards(self):
        return self.journey_towards

    def set_journey_towards(self, journey_towards):
        self.journey_towards = journey_towards

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def __str__(self):
        return str(self.receipt_id)

