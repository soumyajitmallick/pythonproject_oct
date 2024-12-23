from django.db import models

# Create your models here.
class register_master(models.Model):
    name =models.CharField(max_length=50)
    email=models.CharField(max_length=100,primary_key=True)
    mobile=models.CharField(max_length=12)
    password=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    dob=models.DateField()
    role=models.CharField(max_length=30)
    status=models.IntegerField(default=0)
    def __str__(self):
        return self.name
    


class profile_update(models.Model):
    email=models.ForeignKey('register_master',on_delete=models.CASCADE,)
    address=models.CharField(max_length=100)
    image=models.FileField(upload_to='images/')
    upload_doc=models.FileField(upload_to='Document/')
    def __str__(self):
        return f"Profile of {self.email}"