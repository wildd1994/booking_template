from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Booking
from .forms import BookingForm


class BookingList(ListView):
    pass


class BookingDetail(LoginRequiredMixin, DetailView):
    pass


class BookingCreate(CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking_edit.html'
    context_object_name = 'booking'


class BookingUpdate(LoginRequiredMixin, UpdateView):
    pass


class BookingDelete(LoginRequiredMixin, DeleteView):
    pass
