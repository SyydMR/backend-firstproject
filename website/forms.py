from django import forms
from website.models import Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['title', 'message', 'ref_id', 'user_id']

    

