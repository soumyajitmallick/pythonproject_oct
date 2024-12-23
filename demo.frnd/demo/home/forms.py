from django import forms
from .models import *

class userMasterForm(forms.ModelForm):
    class Meta:
        model = UserMaster
        # fields = '__all__'
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

        widgets = {
            'password': forms.PasswordInput(),
        }