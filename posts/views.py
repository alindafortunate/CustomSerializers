from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from .models import BlogPost, Comment
from .serializers import BlogPostSerializer
from rest_framework.response import Response


# Create your views here.
class BlogPostView(generics.ListAPIView):
    model = BlogPost
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class BlogPostViewWithComments(generics.ListAPIView):
    model = BlogPost
    post = BlogPost.objects.get(id=1)
    post1 = post.comments.all()
    queryset = post1
    serializer_class = BlogPostSerializer


@api_view(["GET"])
def post_detail(request, pk):
    post = BlogPost.objects.get(pk=pk)
    serializer = BlogPostSerializer(post)
    return Response(serializer.data)
