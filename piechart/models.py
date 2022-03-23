from django.db import models

# Create your models here.

class Population(models.Model):
    name = models.CharField(max_length=100)
    population = models.IntegerField()
    area = models.IntegerField(null=True)

    class Meta():
        db_table = 'population'
