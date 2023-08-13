from django.urls import path
# Импортируем созданное нами представление
from .views import (
   BookingDetail,
   BookingDelete,
   booking_update,
   my_bookings,
   my_schedule,
   validate_time_slots
)


urlpatterns = [
   path('my_bookings', my_bookings, name='my_booking'),
   path('my_schedule', my_schedule, name='list_booking'),
   path('<int:pk>', BookingDetail.as_view(), name='booking_detail'),
   path('<int:pk>/update/', booking_update, name='booking_update'),
   path('<int:pk>/delete/', BookingDelete.as_view(), name='booking_delete'),
   path('validate_timeslots', validate_time_slots, name='validate_username')
   # path('create/', booking, name='choice_booking')
]
