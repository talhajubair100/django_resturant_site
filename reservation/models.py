from django.db import models
from django.utils import timezone


class Reservation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.IntegerField()
    number_of_persion =models.IntegerField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    

