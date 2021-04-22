from django.db import models

class Tutorial(models.Model):
    name = models.CharField(max_length=90, blank=False, default='')
    photo_url = models.URLField(max_length=200,blank=False, default='')

class Bookings(models.Model):
    booking_time = models.DateTimeField()