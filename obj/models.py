from django.db import models


# Create your models here.
class Garage(models.Model):
    garage_name = models.CharField(max_length=30)
    garage_address = models.TextField()
    garage_status = models.BooleanField()
    garage_owner_name = models.CharField(max_length=30)
    garage_owner_email = models.EmailField()
    garage_owner_contact = models.CharField(max_length=12)

    class Meta():
        db_table = 'garage'