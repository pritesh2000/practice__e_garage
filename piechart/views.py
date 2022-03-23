from cProfile import label
from django.shortcuts import render
from .models import Population

# Create your views here.

def piechart(request):
    labels = []
    data = []

    queryset = Population.objects.all()
    for city in queryset:
        labels.append(city.name)
        data.append(city.population)

    return render(request, "sendmail/pie_chart.html", { 
        'labels' : labels,
        'data' : data,
     })

