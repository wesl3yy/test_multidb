from django.db import models


# Create your models here.

class Hotel(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)


class Room(models.Model):
    VIP = 1
    NORMAL = 2
    ROOM_CHOICES = [
        (VIP, 'Vip'),
        (NORMAL, 'Normal')
    ]
    hotel = models.ForeignKey(Hotel, related_query_name='hotel', on_delete=models.CASCADE)
    room_number = models.IntegerField()
    type = models.IntegerField(choices=ROOM_CHOICES)

