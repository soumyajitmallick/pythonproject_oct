from django.db import models

class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return self.name
       

class add(models.Model):
    f1 = models.CharField(max_length=10)
    f2 = models.CharField(max_length=10) 