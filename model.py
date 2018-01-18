from django.db import models


class owner(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    opening_time = models.IntegerField()
    closing_time = models.IntegerField()


class properties(models.Model):
    owener = models.ForeignKey(Restaurant)
    size = models.IntegerField()


class Booking(models.Model):
     = models.ForeignKey(Table)
    renter = models.IntegerField()
    booking_date_time_start = models.DateTimeField()
    booking_date_time_end = models.DateTi
