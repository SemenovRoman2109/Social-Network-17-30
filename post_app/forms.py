from .models import *
from django import forms
from django.db import transaction
from PIL import Image
from io import BytesIO

MAX_COMPRESSED_IMAGE_SIZE = 5 * 1024 * 1024

class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)
    new_tags = forms.CharField(required=False)
    links = forms.CharField(required=False)
    images = forms.ImageField(required=False)
    
    class Meta:
        model = Post
        fields = ['title', 'topic', 'content']
        
    def __init__(self, *args, author=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.author = author

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
    
    def clean_images(self):
        files = self.files.getlist("images")
        if len(files) > 10:
            raise forms.ValidationError('Кількість зображень має бути менше 10')
        for image in files:
            forms.ImageField().clean(image)
            image.seek(0)
        return files

    @transaction.atomic
    def save(self, commit = True):
        post : Post = super().save(commit=False)
        post.author = self.author
        post.save()
        
        post.tags.set(self.cleaned_data['tags'])
        for tag_name in self.cleaned_data['new_tags']:
            tag, is_created = Tag.objects.get_or_create(name = tag_name)
            post.tags.add(tag)
         
        for url in self.cleaned_data['links']:
            link = PostLink.objects.create(post = post, url = url)

        for image in self.cleaned_data['image']:
            PostImage.objects.create(
                post = post, 
                original_image = image,
                compressed_image = self.compress_image(image)
            )
    
    def compress_image(self, image):
        image.seek(0)
        image = Image.open(image)
        image = image.convert("RGB")
        quality = 85
        width, height = image.size
        while True:
            buffer = BytesIO()
            image.save(buffer, format="JPEG", quality=quality, optimize=True)
            if buffer.tell() < MAX_COMPRESSED_IMAGE_SIZE:
                break
            
            if quality > 35:
                quality -= 10
            else:
                width = int(width*0.9)
                height = int(height*0.9)
                
            
# @transaction.atomic - декоратор який в разі помилки, повернить (відкатить) всі змінення БД які були в функції
# from django.db import transaction

# об'єкт, is_created = Модель.objects.get_or_create(поле=значення) -> 
# отримує об'єкт або створює його (is_created - True/False)

# Валідація зображень в формі:
#   forms.ImageField().clean(image)
#   image.seek(0)