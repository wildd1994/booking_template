from django import forms
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