from django.contrib.auth.models import User
from django import forms

class Editprofile(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','email']