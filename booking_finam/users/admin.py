from django.contrib import admin
from .models import User


class MyUserAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'second_name',
        'last_name',
        'booking_field',
        'email'
    )


admin.site.register(User, MyUserAdmin)
