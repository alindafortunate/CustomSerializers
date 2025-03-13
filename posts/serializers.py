from rest_framework import serializers
from .models import Comment, BlogPost


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "content", "author", "created_at"]


class BlogPostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = BlogPost
        fields = ["id", "title", "author", "content", "created_at", "comments"]
