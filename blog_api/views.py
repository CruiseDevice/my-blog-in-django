# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.shortcuts import get_object_or_404

from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response

from taggit.models import Tag

from blog.models import Post
from .serializers import PostSerializer


@api_view(['GET'])
def post_list(request, tag_slug=None):
    posts = Post.objects.filter(published_date__lte=timezone.now())\
            .order_by('created_date')

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])
    serializer = PostSerializer(posts, many=True)

    return Response(serializer.data)


@api_view(['GET', 'POST'])
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    serializer = PostSerializer(post)
    return Response(serializer.data)
