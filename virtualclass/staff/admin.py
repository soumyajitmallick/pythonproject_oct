from django.contrib import admin
from .models import add_Book,Book_Issued

admin.site.register(add_Book)
admin.site.register(Book_Issued)
