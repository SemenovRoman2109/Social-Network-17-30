from .models import *
from django import forms


class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)
    new_tags = forms.CharField(required=False)
    links = forms.CharField(required=False)
    images = forms.ImageField(required=False)
    
    class Meta:
        model = Post
        fields = ['title', 'topic', 'content']
        