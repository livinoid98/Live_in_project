from django import forms
from django.forms import TextInput, Textarea
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': TextInput(attrs={'class':'floatLabel', 'placeholder':'Title'}),
            'content' : Textarea(attrs={'class':'floatLabel', 'placeholder':'Content'}),
        }