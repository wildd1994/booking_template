from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Booking
from .forms import BookingForm


class BookingList(ListView):
    pass


class BookingDetail(LoginRequiredMixin, DetailView):
    pass


class BookingUpdate(LoginRequiredMixin, UpdateView):
    pass


class BookingDelete(LoginRequiredMixin, DeleteView):
    pass


def booking(request):
    dict_obj = {}
    return render(request, 'booking.html', dict_obj)
