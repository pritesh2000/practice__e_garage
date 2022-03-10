from .models import Employee
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView

# Create your views here.
class CreateEmployee(CreateView):
    model = Employee
    fields = ['emp_name', 'emp_email', 'emp_password', 'emp_phone','emp_dob']
    template_name = 'employee/create_employee.html'
    success_url = '/employee/view'
    print("template_view")

class ViewEmployee(ListView):
    model = Employee
    employees = '__all__'
    context_object_name = 'employees'
    template_name = 'employee/view_employee.html'
    

