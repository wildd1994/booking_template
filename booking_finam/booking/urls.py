from django.urls import path
# Импортируем созданное нами представление
from .views import (
   BookingList,
   BookingDetail,
   BookingCreate,
   BookingDelete,
   BookingUpdate
)


urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', BookingList.as_view(), name='booking_list'),
   path('<int:pk>', BookingDetail.as_view(), name='booking_detail'),
   path('create/', BookingCreate.as_view(), name='booking_create'),
   path('<int:pk>/update/', BookingUpdate.as_view(), name='booking_update'),
   path('<int:pk>/delete/', BookingDelete.as_view(), name='booking_delete'),
]
