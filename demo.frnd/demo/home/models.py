from django.db import models

# Create your models here.


class UserMaster(models.Model):
    username = models.CharField(max_length=100, unique = True)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.username