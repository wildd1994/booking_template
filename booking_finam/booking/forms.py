from django import forms
from django.core.exceptions import ValidationError

from .models import Booking


class BookingForm(forms.ModelForm):
    description = forms.CharField(min_length=20)
    date_booking = forms.DateField(widget=forms.SelectDateWidget, label='Дата бронирования')
    start_time_booking = forms.TimeField(label='Время начала бронирования')
    end_time_booking = forms.TimeField(label='Время окончания бронирования')

    class Meta:
        model = Booking
        fields = [
            'who_booking',
            'who_booked',
            'date_booking',
            'start_time_booking',
            'end_time_booking',
            'description'
        ]

    def clean(self):
        cleaned_data = super().clean()
        time_start = cleaned_data.get("start_time_booking")
        time_end = cleaned_data.get("end_time_booking")
        if time_start > time_end:
            raise ValidationError({
                "end_time_booking": "Время окончания не может быть меньше времени начала."
            })

        return cleaned_data
