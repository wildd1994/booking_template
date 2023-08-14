from datetime import datetime

from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.generic import DetailView, DeleteView
from django.urls import reverse_lazy

from users.models import User
from .models import Booking
from .forms import BookingForm


class BookingDetail(LoginRequiredMixin, DetailView):
    model = Booking
    template_name = 'booking_detail.html'
    success_url = reverse_lazy('list_product')


class BookingDelete(LoginRequiredMixin, DeleteView):
    model = Booking
    template_name = 'booking_delete.html'
    success_url = reverse_lazy('list_booking')


def booking_update(request, **kwargs):
    booking_id = kwargs.get('pk')
    booking = Booking.objects.get(pk=booking_id)
    if booking.who_booking.pk != request.user.pk and booking.who_booked.pk != request.user.pk:
        return render(request, '403.html', {})
    if not request.user.is_authenticated:
        return render(request, '403.html', {})
    if request.POST:
        who_booked = request.POST.get('who_booked')
        who_booking = request.user.pk
        date_booking = request.POST.get('date_booking')
        time_start = request.POST.get('start_time_booking')
        time_end = request.POST.get('end_time_booking')
        description = request.POST.get('description')
        data = {
            'who_booked': who_booked,
            'who_booking': who_booking,
            'date_booking': date_booking,
            'start_time_booking': time_start,
            'end_time_booking': time_end,
            'description': description
        }
        f = BookingForm(data=data, instance=booking)
        if f.is_valid():
            f.save()
            # это можно через селери сделать
            send_message(f.instance, 'change')
            return HttpResponseRedirect(booking.get_absolute_url())
        else:
            return render(request, "booking_edit.html", {'booking': booking, 'errors': f.errors})
    else:
        users_booked = User.objects.filter(booking_field='booked').exclude(pk=booking.who_booked.pk)
        dict_obj = {
            'bookings_people': users_booked,
            'booking': booking,
            'booking_id': booking_id,
            'today': datetime.today().strftime('%Y-%m-%d')
        }
        return render(request, "booking_edit.html", dict_obj)


def my_schedule(request):
    if request.user.is_authenticated:
        user = User.objects.get(pk=request.user.pk)
        if user.booking_field == 'booked':
            bookings = Booking.objects.filter(who_booked=user.pk).all()
            dict_obj = {
                'bookings': bookings,
                'my_schedule': True
            }
            return render(request, 'booking_list.html', dict_obj)
        else:
            dict_obj = {
                'reason': 'Необходимо быть объектом записи'
            }
            return render(request, '403.html', dict_obj)
    dict_obj = {
        'reason': 'Необходимо зарегистрироваться'
    }
    return render(request, '403.html', dict_obj)


def create_booking(request):
    if not request.user.is_authenticated:
        dict_obj = {
            'reason': 'Необходимо зарегистрироваться'
        }
        return render(request, '403.html', dict_obj)
    if request.POST:
        who_booked = request.POST.get('who_booked')
        who_booking = request.user.pk
        date_booking = request.POST.get('date_booking')
        time_start = request.POST.get('start_time_booking')
        time_end = request.POST.get('end_time_booking')
        description = request.POST.get('description')
        data = {
            'who_booked': who_booked,
            'who_booking': who_booking,
            'date_booking': date_booking,
            'start_time_booking': time_start,
            'end_time_booking': time_end,
            'description': description
        }
        f = BookingForm(data=data)
        if f.is_valid():
            f.save()
            # это можно через селери сделать
            send_message(f.instance, 'create')
            return HttpResponseRedirect(f.instance.get_absolute_url())
        else:
            return render(request, "booking_edit.html", {'booking': f.instance, 'errors': f.errors})
    else:
        users_booked = User.objects.filter(booking_field='booked')
        dict_obj = {
            'bookings_people': users_booked,
            'today': datetime.today().strftime('%Y-%m-%d')
        }
        return render(request, "booking_edit.html", dict_obj)


def my_bookings(request):
    if request.user.is_authenticated:
        user_id = request.user.pk
        bookings = Booking.objects.filter(who_booking=user_id).all()
        dict_obj = {
            'bookings': bookings,
            'my_bookings': True
        }
        return render(request, 'booking_list.html', dict_obj)
    dict_obj = {
        'reason': 'Необходимо зарегистрироваться'
    }
    return render(request, '403.html', dict_obj)


def validate_time_slots(request):
    if is_ajax(request):
        date_booking = request.GET.get('date_booking')
        time_start = request.GET.get('start_time_booking')
        if not time_start:
            response = {
                'errors': 'Отсутствует время старта',
                'status': 'false'
            }
            return JsonResponse(response,  status=404)
        time_end = request.GET.get('end_time_booking')
        if not time_end:
            response = {
                'errors': 'Отсутствует время окончания',
                'status': 'false'
            }
            return JsonResponse(response, status=404)
        user = request.GET.get('who_booked', None)
        booking_pk = request.GET.get('booking_id')
        if booking_pk:
            bookings = Booking.objects.filter(who_booked=user, date_booking=date_booking).exclude(pk=booking_pk)
        else:
            bookings = Booking.objects.filter(who_booked=user, date_booking=date_booking)
        is_taken = check_time(bookings, time_start, time_end)
        response = {
            'is_taken': is_taken
        }
        return JsonResponse(response)


def check_time(bookings, time_start, time_end) -> bool:
    time_start_obj = datetime.strptime(time_start, '%H:%M').time()
    time_end_obj = datetime.strptime(time_end, '%H:%M').time()
    print(time_start_obj, time_end_obj)
    for booking in bookings:
        start_booking = booking.start_time_booking
        end_booking = booking.end_time_booking
        print(start_booking, end_booking)
        is_before = time_end_obj < start_booking
        is_after = time_start_obj > end_booking
        print(f'{is_before} - до бронирования')
        print(f'{is_after} - после бронирования')
        if not is_before:
            if not is_after:
                return True
    return False


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def send_message(instance, action):
    url = instance.get_absolute_url()
    if action == 'change':
        subject = 'Изменение в бронировании!'
        msg = (f'{instance.who_booking.username}, одно из бронирований изменено!\n\n'
               f'http://127.0.0.1:8000{url}')
    else:
        subject = 'Новое бронирование!'
        msg = (f'{instance.who_booking.username}, у вас новое бронирование!\n\n'
               f'http://127.0.0.1:8000{url}')
    send_mail(
        subject=subject,
        message=msg,
        from_email=None,
        recipient_list=[instance.who_booking.email, instance.who_booked.email],
    )
