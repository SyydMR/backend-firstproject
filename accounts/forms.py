from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    profile_pic = forms.ImageField()
    phone = forms.CharField(max_length=30)
    national_code = forms.CharField(max_length=10)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields
    

