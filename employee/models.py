from django.db import models

from generic.models import BaseField

# Create your models here.
class Employee(BaseField):
    emp_name = models.CharField(max_length=50)
    emp_dob = models.DateField()
    emp_email = models.EmailField(max_length=50)
    emp_password = models.CharField(max_length=30)
    emp_phone = models.CharField(max_length=15)

    class Meta():
        db_table = 'employee'

