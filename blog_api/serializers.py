from django.contrib.auth.models import User, Group
from rest_framework import serializers

from blog.models import Post, Comment, Tag
from .relations import TagRelatedField, CommentRelatedField


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    author = serializers.CharField(source='author.username', read_only=True)
    commentsList = CommentRelatedField(many=True, required=False, source='comments')
    tagList = TagRelatedField(many=True, required=False, source='tags')

    class Meta:
        model = Post
        fields = ['id', 'author', 'slug', 'title', 'text', 'created_date',
                  'published_date', 'status', 'commentsList', 'tagList']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
