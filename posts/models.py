from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import CustomUser

CustomUser = get_user_model()


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(
        BlogPost, on_delete=models.CASCADE, related_name="comments", null=True
    )
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="posts", null=True
    )
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.content[:10]}"
