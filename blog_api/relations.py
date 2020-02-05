from rest_framework import serializers

from blog.models import Tag, Comment


class TagRelatedField(serializers.RelatedField):

    def get_queryset(self):
        return Tag.objects.all()

    def to_representation(self, value):
        return value.tag


class CommentRelatedField(serializers.RelatedField):

    def get_queryset(self):
        return Comment.objects.all()

    def to_representation(self, value):
        return {
            'body': value.body,
            'name': value.name,
            'email': value.email,
            'created': value.created,
            'updated': value.updated,
        }