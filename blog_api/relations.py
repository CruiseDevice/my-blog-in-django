from rest_framework import serializers

from blog.models import Tag, Comment


class TagRelatedField(serializers.RelatedField):

    def get_queryset(self):
        return Tag.objects.all()

    def to_representation(self, value):
        return value.tag
