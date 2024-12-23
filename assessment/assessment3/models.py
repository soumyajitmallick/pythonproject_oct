from django.db import models
from django.utils import timezone

# Create your models here.
class employee(models.Model):
    emp_id=models.AutoField(primary_key=True)
    emp_name=models.CharField(max_length=100)
    emp_phone=models.CharField(max_length=100)
    emp_email=models.EmailField(max_length=50)
    def __str__(self):
        return f'{self.emp_name} - {self.emp_name}'

class leave_Master(models.Model):
    leave_id=models.AutoField(primary_key=True)
    leave_name=models.CharField(max_length=30)
    def __str__(self):
        return f'{self.leave_name} - {self.leave_name}'

class leave_emp_assign(models.Model):
    sl_no=models.AutoField(primary_key=True)
    emp_id=models.ForeignKey(employee,on_delete=models.CASCADE)
    leave_id=models.ForeignKey(leave_Master, on_delete=models.CASCADE)
    no_of_assigned_leave=models.IntegerField
    def __str__(self):
        return f'{self.emp_id} - {self.leave_id}'

class leave_apply(models.Model):
    sl_no=models.AutoField(primary_key=True)
    emp_id=models.ForeignKey(employee,on_delete=models.CASCADE)
    date_of_leave=models.DateField(default=timezone.now)
    leave_emp_id=models.ForeignKey(leave_emp_assign,on_delete=models.CASCADE)
    no_of_apply_leave=models.IntegerField()           
    def __str__(self):
        return f'{self.emp_id} - {self.leave_emp_id}'
    def save(self,*args,**kwargs):
        if self.no_of_apply_leave <= self.leave_emp_id.no_of_aval_leave :
            self . leave_emp_id . no_of_aval_leave -= self.no_of_apply_leave
            self . leave_emp_id . save()
            return super(leave_apply,self).save(*args,**kwargs)
        else:
            raise ValueError(f'No of aval leave is {self.leave_emp_id.no_of_aval_leave}')