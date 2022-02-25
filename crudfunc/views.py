from django.http import HttpResponse
from django.shortcuts import render
from .models import Owner

# Create your views here.
def addOwner(request):
    own = Owner(owner_name = 'pritesh', owner_password = 'pritesh@123', owner_contact = '9998509177', owner_email = 'pritesh@gmail.com', owner_address = 'bhavnagar', owner_dob = '1121-12-12', owner_age = 22)
    own.save()
    return HttpResponse("Owner added...")

def viewOwner(request):
    owns = Owner.objects.all().values()
    ownlist = []
    for i in range(len(owns)):
        for j in owns[i].values():
            ownlist.append(j)
    return render(request, 'crudfunc/view.html', {'own' : ownlist})

def deleteOwner(request):
    own = Owner.objects.get(id = 2)
    own.delete()
    return HttpResponse("Owner deleted...")

def updateOwner(request):
    own = Owner.objects.get(id = 3)
    own.owner_name = 'mahesh'
    own.owner_password = 'mahesh@123'
    own.save()
    return HttpResponse("Owner data updated...")
    