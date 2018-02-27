# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post
from django.utils import timezone
from .forms import PostForm
# Create your views here.

class PostListView(ListView):
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('created_date')
    context_object_name = 'posts'
    paginate_by = 3
    template_name = "blog/post/post_list.html"

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('created_date')
    return render(request,'blog/post/post_list.html',{'posts':posts})

def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request, 'blog/post/post_detail.html',{'post':post})

def post_new(request):
    if request.method == "POST":
        form=PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author=request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)

    else:
        form=PostForm()
    return render(request,'blog/post/post_edit.html',{'form':form})


def post_edit(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method=="POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request,'blog/post/post_edit.html',{'form':form})

def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request,'blog/post/post_draft_list.html',{'posts':posts})

# def post_share(request, post_id):
#     # Retrieve post by id
#     post = get_object_or_404(Post, id=post_id, )