from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def sendmail(request):
    subject = 'welcome'
    message = 'Hello User!!!!!'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['priteshptadvi29@gmail.com', 'pandarjaimin120@gmail.com']
    send_mail(subject,message,email_from,recipient_list)
    return HttpResponse("SEND MAIL FOR REGISTRATION...")

