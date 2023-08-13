from django.db import models
from django.shortcuts import reverse

from users.models import User


class Booking(models.Model):

    who_booking = models.ForeignKey(User, on_delete=models.CASCADE, related_name='who_booking')
    who_booked = models.ForeignKey(User, on_delete=models.CASCADE, related_name='who_booked')
    date_booking = models.DateField()
    start_time_booking = models.TimeField()
    end_time_booking = models.TimeField()
    description = models.TextField()

    def get_absolute_url(self):
        return reverse("booking_detail", kwargs={"pk": self.pk})
