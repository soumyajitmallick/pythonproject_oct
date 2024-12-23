from django.contrib import admin

# Register your models here.
from .models import*
admin.site.register(subject)
admin.site.register(chapter)
admin.site.register(question)