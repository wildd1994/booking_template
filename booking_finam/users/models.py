from django.db import models
from django.contrib.auth.models import AbstractUser

MY_CHOICES = (
        ('booked', 'Ко мне будут записываться'),
        ('booking', 'Я буду записываться'),
    )


class User(AbstractUser):
    booking_field = models.CharField(choices=MY_CHOICES, blank=False, max_length=7)
    second_name = models.CharField(blank=True, max_length=50)
    username = models.CharField(blank=False, unique=True, max_length=50)
