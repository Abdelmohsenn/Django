from django.urls import path
from Post.views import PostView

urlpatterns = [
    path('posts/', PostView.as_view(), name='post_list'),
]