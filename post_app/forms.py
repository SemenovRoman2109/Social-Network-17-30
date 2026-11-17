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

    def clean_new_tags(self):
        result = []
        for tag in self.data.getlist("new_tags"):
            tag = tag.strip()
            if len(tag) > 30:
                raise forms.ValidationError("Тег не может быть длиннее 30-и символов")
            if tag not in result:
                result.append(tag)
        return result

    def clean_links(self):
        result =[]
        for link in self.data.getlist("links"):
            link = link.strip()
            if link:
                result.append(forms.URLField().clean(link))
        return result

    def save(self, commit = True):
        return super().save(commit)
