from .views import ViewGarage 
from django.urls import path

urlpatterns = [
    path('list/', ViewGarage.as_view())
]
