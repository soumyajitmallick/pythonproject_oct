from django.db import models
from datetime import date
# Create your models here.

class add_Book(models.Model):
    ISBN_No = models.CharField(max_length=100, primary_key=True)  
    Book_Name = models.CharField(max_length=100)  
    Author_Name = models.CharField(max_length=100)  
    def __str__(self):
        return self.Book_Name

class Book_Issued(models.Model):
    Book_Issued_id=models.AutoField(primary_key=True)
    Issued_Date=models.DateField(default=date.today)
    mobile=models.CharField(max_length=10)
    Book_Name=models.ForeignKey('add_Book',on_delete=models.CASCADE,default=None)
    