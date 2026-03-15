from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from Post.models import Post, Comment
from datetime import datetime
from .serializers import PostSerializer
# Create your views here.

class PostView(APIView):
    # def get(self, request):
    #     posts = Post.objects.all()
    #     posts_data = [post for post in posts.values()]
    #     for post in posts_data:
    #         # problem N+1
    #         commentsList = [comment for comment in Comment.objects.filter(post_id=post['id']).values()]
    #         post['created_at'] = post['created_at'].strftime('%Y-%m-%d %H:%M:%S')
    #         post['Comments_count'] = len(commentsList)
    #         post['comments'] = commentsList
    #     return JsonResponse({'posts': posts_data})
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
