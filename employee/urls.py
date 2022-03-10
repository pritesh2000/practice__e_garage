from .views import CreateEmployee, ViewEmployee
from django.urls import path


urlpatterns = [
    path('create/', CreateEmployee.as_view(), name= 'create_employee'),
    path('view/', ViewEmployee.as_view(), name= 'view_employee'),
]
