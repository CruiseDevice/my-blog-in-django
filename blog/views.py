# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post, Comment
from django.utils import timezone
from .forms import PostForm, CommentForm, EmailPostForm
from django.db.models import Count
# Create your views here.

class PostListView(ListView):
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('created_date')
    context_object_name = 'posts'
    paginate_by = 3
    template_name = "blog/post/post_list.html"

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('created_date')
    return render(request,
            'blog/post/post_list.html',{
                'posts':posts
    })

def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    # new_comment = None
    # List of active comments for this post
    comments = post.comments.filter(active=True)
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create comment object but don't save it to database
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 
            'blog/post/post_detail.html',{
                'post':post,
                'comment_form':comment_form,
                'comments':comments
    })

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
    return render(request,
            'blog/post/post_edit.html',{
                'form':form
    })


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
    return render(request,
            'blog/post/post_edit.html',{
                'form':form,
                'post':post
    })

def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request,
            'blog/post/post_draft_list.html',{
                'posts':posts
    })

def post_share(request, pk):
    # Retrieve post by id
    post = get_object_or_404(Post, pk=pk, status='published')
    if request.method == "POST":
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            # ... send email
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html',{
            'post':post,
            'form':form
    })