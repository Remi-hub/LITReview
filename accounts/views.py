# Create your views here.
from django.contrib.auth.views import LoginView as BaseLoginView
from django.urls import reverse_lazy
from django.views import generic

from accounts.form import UserCreationForm


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class LoginView(BaseLoginView):
    pass


