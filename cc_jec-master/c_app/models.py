from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 128, default='')
    last_name = models.CharField(max_length = 128, default='')
    semester = models.IntegerField(max_length = 128, default=0)
    branch = models.CharField(max_length = 128, default='')
    contact = models.IntegerField(max_length = 128, default=0)
    town = models.CharField(max_length = 128, default='')
    email = models.EmailField(max_length = 254, unique = True, default='')
