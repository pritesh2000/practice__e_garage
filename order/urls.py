from django.urls import path
from .views import CreatePark, CreateOrder
urlpatterns = [
    path('create_park/', CreatePark.as_view(), name= 'create_park'),
    path('create_order/', CreateOrder.as_view(), name = 'create_order'),
]
