from django.contrib import admin
from .models import *

# Register your models here.

class userAdmin(admin.ModelAdmin):
    fields = [ 'first_name', 'last_name', 'email','username',  'password']
    search_fields = ['username', 'email']
    list_filter = ['username', 'email','first_name']
    list_display = ['first_name', 'last_name', 'email', 'username']
    list_editable = [ 'last_name', 'email', 'username']
    

admin.site.register(UserMaster, userAdmin)

admin.site.site_header = "Demoadmin"
admin.site.site_title = "adminpaneldemo"
admin.site.index_title = "welcome to your admin panel of demo"