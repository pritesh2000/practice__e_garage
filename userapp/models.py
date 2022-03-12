from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(_('email address'), max_length=70 ,unique=True)
    
    phone_regex = RegexValidator(regex=r'^[7-9]{1}\d{9}', message="Phone number must be entered in the format: '9999999999'")
    phone_number = models.CharField(validators=[phone_regex],max_length=10, blank=True, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


    class Meta():
        db_table = 'User'

    def __str__(self):
        return self.username


