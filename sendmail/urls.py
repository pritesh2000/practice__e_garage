from sendmail import views
from django.urls import path

urlpatterns = [
    path('sendmail/', views.sendmail, name="send_mail"),
]
