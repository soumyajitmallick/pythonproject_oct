from django.db import models
from signup.models import signup_master
# Create your models here.
options=[
    ('Deposit','Deposit'),
    ('Withdraw','Withdraw')
]

class Transaction (models.Model):
    account_no=models.ForeignKey(signup_master,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=40,decimal_places=5)
    date=models.DateTimeField(auto_now_add=True)
    type = models.CharField( max_length = 40, choices= options, default='Deposit' )