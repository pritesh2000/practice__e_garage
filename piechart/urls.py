from django.urls import path
from piechart import views

urlpatterns = [
    path('', views.piechart, name='pie_chart'),
]
