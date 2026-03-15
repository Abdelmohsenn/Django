from rest_framework import serializers
from .models import Post, Comment
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        
    def to_representation(self, instance): # self is the serializer instance, instance is the model instance
        rep = super().to_representation(instance)
        rep['created_at'] = instance.created_at.strftime('%Y-%m-%d %H:%M:%S')
        rep['Comments_count'] = instance.comments.count()
        rep['comments'] = CommentSerializer(instance.comments.all(), many=True).data
        return rep
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['created_at'] = instance.created_at.strftime('%Y-%m-%d %H:%M:%S')
        return rep