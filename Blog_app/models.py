from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=225)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', null = True, blank = True)
    publched_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    content = models.TextField()
    publched_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
