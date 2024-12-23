from django.db import models

# Create your models here.

class signup_master(models.Model):
    account_no=models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    mobile_no=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    status=models.IntegerField(default=0)
    def __repr__(self):
        return str ( self.account_no )