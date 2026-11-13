from django.urls import path
from .views import *

urlpatterns = [
    path("", PostView.as_view(), name = "posts"),
    path("create/", CreatePostView.as_view(), name = "create_post")
]