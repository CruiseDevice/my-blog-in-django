from django.contrib.auth.models import User, Group
from rest_framework import serializers

from blog.models import Post, Comment, Tag
from .relations import TagRelatedField


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    tags = TagRelatedField(many=True)
    class Meta:
        model = Post
        fields = ['id', 'author', 'slug', 'title', 'text', 'created_date',
                  'published_date', 'status', 'comments', 'tags']
