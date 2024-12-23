from django.db import models

# Create your models here.
class subject(models.Model):
    subject_id=models.AutoField(primary_key=True)
    subject_name=models.CharField(max_length=100)
    def __str__(self):
        return self.subject_name

class chapter(models.Model):
    subject_name=models.ForeignKey(subject,on_delete=models.CASCADE)
    chapter_id=models.AutoField(primary_key=True)
    chapter_name=models.CharField(max_length=100)
    def __str__(self):
        return self.chapter_name

class question(models.Model):
    subject_name=models.ForeignKey(subject,on_delete=models.CASCADE)
    chapter_name=models.ForeignKey(chapter,on_delete=models.CASCADE)
    question_id=models.AutoField(primary_key=True)
    question=models.CharField(max_length=500)
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    answer=models.CharField(max_length=100, choices=(
        ('option1' , 'option1'),
        ('option2' , 'option2'),
        ('option3' , 'option3'),
        ('option4' , 'option4'),
                    ))
    def __str__(self):
        return self.question