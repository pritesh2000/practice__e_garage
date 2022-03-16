from django.shortcuts import render

from userapp.models import User
# from .models import *
from .forms import UserForm
from django.views.generic import FormView, CreateView, DeleteView, UpdateView, DetailView, ListView
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

class BaseRegisterView(SuccessMessageMixin, FormView):
    form_class = UserForm
    template_name = 'userportal/registration.html'
    success_url = '/user/user-login'

    def form_valid(self, form):
        user = form.save()
        user.set_password(user.password)
        user.save()
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        username = cleaned_data["username"]
        return username + "- User Created Successfully!!!"

class UserLoginView(LoginView):
    template_name = 'userportal/user_login.html'
    success_url = '/user/index'

def index(request):
    return render(request, 'userportal/index.html')


class ViewUser(ListView):
    model = User
    users = model.objects.all()
    context_object_name = 'users'
    template_name = 'userportal/view_user.html'

class DetailUser(DetailView):
    model = User
    template_name = 'userportal/detail_user.html'
    context_object_name = 'user'

class DeleteUser(DeleteView):
    model = User
    template_name = 'userportal/delete_user.html'
    success_url = '/user/view'

class UpdateUser(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'userportal/update_user.html'
    success_url = '/user/view'
