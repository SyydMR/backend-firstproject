from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User

class CustomUserCreationForm(UserCreationForm):
    # profile_pic = forms.ImageField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    phone = forms.CharField(max_length=30)
    national_code = forms.CharField(max_length=10)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields

    

