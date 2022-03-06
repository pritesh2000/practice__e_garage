from django.shortcuts import render
from .models import Park, Order
from django.views.generic.edit import CreateView
# Create your views here.

class CreatePark(CreateView):
    model = Park
    fields = '__all__'
    template_name = 'park/create_park.html'
    success_url = '/order/create_order'


class CreateOrder(CreateView):
    model = Order
    fields = '__all__'
    template_name = 'park/create_order.html'
    success_url = '/order/create_park'

