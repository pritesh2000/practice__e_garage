from userapp import views
from userapp.views import BaseRegisterView, UserLoginView
from django.urls import path, include


urlpatterns = [
    path('user-registration/', BaseRegisterView.as_view(), name = "user_registration"),
    path('user-login/', UserLoginView.as_view(), name = "user_login"),
    path('index/', views.index)

]
