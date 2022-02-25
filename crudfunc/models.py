from django.db import models

# Create your models here.
class Owner(models.Model):
    owner_name = models.CharField(max_length=30)
    owner_password = models.CharField(max_length=20)
    owner_contact = models.CharField(max_length=12,null=True)
    owner_email = models.EmailField(max_length=30,null=True)
    owner_address = models.TextField(max_length=50,null=True)
    owner_dob = models.DateField(null=True)
    owner_age = models.IntegerField(null=True)

    class Meta():
        db_table = 'owner'