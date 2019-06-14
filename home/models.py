from django.db import models
from login.models import User
# Create your models here.


class Destination(models.Model):
    name = models.CharField(max_length=64, unique=True, null=False)
    description = models.TextField(blank=True)
    background = models.ImageField(upload_to='background_images')

    def __str__(self):
        return str(self.name)


class Lodging(models.Model):
    name = models.CharField(max_length=64, unique=True, null=False)
    description = models.TextField(blank=True)
    background = models.ImageField(upload_to='background_images')
    address = models.CharField(max_length=128, unique=False, blank=False)
    contactno = models.CharField(max_length=20)
    website = models.URLField(blank=True)
    place = models.ForeignKey(
        Destination, on_delete=models.PROTECT, related_name='lodgings')

    def __str__(self):
        return str(self.name)


class Room(models.Model):
    name = models.CharField(max_length=64, unique=False, null=False)
    image = models.ImageField(upload_to='room_images')
    capacity = models.IntegerField(null=False)
    size = models.IntegerField(null=False)
    features = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=False)
    host = models.ForeignKey(
        Lodging, on_delete=models.PROTECT, related_name='rooms')

    def __str__(self):
        return str(self.id)
        # return "%s (%s)" % (
        #     str(self.id),
        #     ", ".join(str(booking.id) for booking in self.bookings.all()),
        # )


class Booking(models.Model):
    startdate = models.DateField(null=False)
    enddate = models.DateField(null=False)
    no_of_people = models.IntegerField(null=False)
    no_of_rooms = models.IntegerField(null=False)
    total_cost = models.DecimalField(max_digits=12, decimal_places=2, blank=False)
    room = models.ForeignKey(
        Room, on_delete=models.PROTECT, related_name='bookings', null=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reservation_holder', null=False)

    def __str__(self):
        return str(self.id)

# class Package(models.Model):
