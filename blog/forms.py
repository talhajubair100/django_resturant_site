from django import forms
from .models import Coment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Coment
        fields = [
            'content'
        ]
