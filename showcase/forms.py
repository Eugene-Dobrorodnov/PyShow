from django import forms
from showcase.models import Comment


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['create_date']
