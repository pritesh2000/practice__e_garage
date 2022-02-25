# for home app and UserHome model

from home import views
from django.urls import path

urlpatterns = [
    path('add/', views.addUser),
]

