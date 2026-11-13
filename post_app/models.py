from django.db import models
from user_app.models import User

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return f'<Tag: #{self.name}>'

class Post(models.Model):
    title = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='posts')
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'posts')
    
    def __str__(self):
        return f"<Post: {self.title}, from user {self.author.username}>"

class PostLink(models.Model):
    url = models.URLField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="links")

    def __str__(self):
        return f'<Link: {self.url}, for {self.post.title}>'

class PostImage(models.Model):
    original_image = models.ImageField(upload_to = "posts/original_images")
    compressed_image = models.ImageField(upload_to = "posts/compressed_images")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="images")
    
    def __str__(self):
        return f"<PostImage: for {self.post.title}>"