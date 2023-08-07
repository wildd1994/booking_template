from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class BookingList(ListView):
    pass


class BookingDetail(LoginRequiredMixin, DetailView):
    pass


class BookingCreate(LoginRequiredMixin, CreateView):
    pass


class BookingUpdate(LoginRequiredMixin, UpdateView):
    pass


class BookingDelete(LoginRequiredMixin, DeleteView):
    pass
