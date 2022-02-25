from django.db import models

# Create your models here.
class UserHome(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField()
    user_password = models.CharField(max_length=20)
    user_contact = models.IntegerField()
    user_age = models.IntegerField()
    user_address = models.TextField()
    user_dob = models.DateField()

    class Meta():
        db_table = 'userhome'