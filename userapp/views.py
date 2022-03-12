from django.shortcuts import render
# from .models import *
from .forms import UserForm
from django.views.generic import FormView
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.

class BaseRegisterView(SuccessMessageMixin, FormView):
    form_class = UserForm
    template_name = 'userportal/registration.html'
    success_url = '/user/user-login'

    def form_valid(self, form):
        user = form.save()
        print("hello")
        user.set_password(user.password)
        user.save()
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        username = cleaned_data["username"]
        return username + "- User Created Successfully!!!"


class UserLoginView(LoginView):
    template_name = 'userportal/user_login.html'
    success_url = '/user/home'

def index(request):
    return render(request, 'userportal/index.html')