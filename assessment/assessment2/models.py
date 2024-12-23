from django.db import models
from django.utils import timezone
# Create your models here.
class Product_Master(models.Model):
    prodID=models.AutoField(primary_key=True)
    prodName=models.CharField(max_length=30)
    prodRate=models.CharField(max_length=30)
    prodQty=models.CharField(max_length=30)
    def __str__(self):
        return self.prodName
    
class Order_Master(models.Model):
    orderID=models.AutoField(primary_key=True)
    orderDate=models.DateField(default=timezone.now)
    prodID=models.IntegerField()
    prodRate=models.IntegerField()
    orderQty=models.IntegerField()
    orderValue=models.BigIntegerField()