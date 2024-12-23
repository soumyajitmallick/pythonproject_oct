from django.db import models
from faculty.models import *
# Create your models here.
class SubmitAnswer(models.Model):
    answer_id=models.AutoField(primary_key=True)
    subject_id=models.ForeignKey(subject,on_delete=models.CASCADE)
    chapter_id=models.ForeignKey(chapter,on_delete=models.CASCADE)
    question_id=models.ForeignKey(question,on_delete=models.CASCADE)
    Answer=models.CharField(max_length=20)

    