from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm
from django.http import JsonResponse
from .models import Tag



# Create your views here.
class PostView(LoginRequiredMixin,TemplateView):
    template_name = 'post_app/posts.html'
    
    def get_context_data(self):
        return {
            "tags": Tag.objects.all()[:10]
        }
        

class CreatePostView(LoginRequiredMixin, CreateView):
    forms_class = PostForm
    http_method_names = ["post"]
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['author'] = self.request.user
        return kwargs
    
    def form_valid(self, form: PostForm):
        ...
        return JsonResponse({"success": True})
    
    def form_inavlid(self, form: PostForm):
        return JsonResponse({"success": False, "errors": form.errors})

# http_method_names = ["post"] - 
# в класі відображення вказує які види запитів приймає сторінка

# Щоб в форму передати параметри з views (наприклад користувача):
# У views метод -> 
#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         Змінення kwargs
#         return kwargs
# у формі їх потрібно отримати -> створити метод __init__ з потрібним параметром