from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from .models import User


class MyCreationForm(UserCreationForm):
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Подтверждение пароля", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'booking_field',
            'second_name'
        ]
        labels = {
            'email': _("Электронная почта"),
            'first_name': _('Имя'),
            'last_name': _('Фамилия'),
            'second_name': _('Отчество'),
            'booking_field': _('Выбор услуги')
        }
