from django.db import models

import users.models


class Booking(models.Model):

    who_booking = models.ForeignKey(users.models.User, on_delete=models.CASCADE, related_name='who_booking')
    who_booked = models.ForeignKey(users.models.User, on_delete=models.CASCADE, related_name='who_booked')
    date_booking = models.DateField()
    start_time_booking = models.TimeField()
    end_time_booking = models.TimeField()
    description = models.TextField()
