from django.db import models

# Create your models here.

class Menu(models.Model):
    ID = models.PositiveSmallIntegerField(primary_key=True)
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.PositiveSmallIntegerField()

class Booking(models.Model):
    ID = models.PositiveIntegerField(primary_key=True)
    Name = models.CharField(max_length=255)
    No_of_guests = models.PositiveSmallIntegerField()
    BookingDate = models.DateTimeField()