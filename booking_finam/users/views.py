from django.views.generic.edit import CreateView

from .forms import MyCreationForm
from .models import User


class SignUpView(CreateView):
    model = User
    form_class = MyCreationForm
    success_url = '/registration/login'
    template_name = 'registration/signup.html'
