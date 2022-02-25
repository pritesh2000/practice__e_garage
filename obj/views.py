from django.views.generic.list import ListView
from django.shortcuts import render
from .models import Garage

# Create your views here.
class ViewGarage(ListView):
    model = Garage
    garage_detail = model.objects.all()
    template_name = 'obj/garage_detail.html'
    context_object_name = 'garage_detail'

    def listGarage(request):
        return render(request, 'obj/obj.html') 
