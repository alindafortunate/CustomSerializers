from django.db import models


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)


class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(
        BlogPost, on_delete=models.CASCADE, related_name="blogposts"
    )
    created_at = models.DateField(auto_now_add=True)
