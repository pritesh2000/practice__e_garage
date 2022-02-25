from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def addUser(request):
    # return HttpResponse("User is Added")
    return render(request, 'home/home.html')