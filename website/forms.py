from django import forms
from website.models import Comment 
from accounts.models import User


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['title', 'message', 'ref_id', 'user_id']

    

class PanelForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone', 'username']
