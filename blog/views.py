# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.utils import timezone
from django.db.models import Count
from django.core.mail import send_mail

from taggit.models import Tag

from .models import Post, Comment
from .forms import PostForm, CommentForm, EmailPostForm


def post_list(request, tag_slug=None):
    posts = Post.objects.filter(published_date__lte=timezone.now())\
                .order_by('created_date')
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])

    paginator = Paginator(posts, 2)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages())

    return render(request, 'blog/post/post_list.html', {
        'page': page,
        'posts': posts,
        'tag': tag
    })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
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
    return render(request, 'blog/post/post_detail.html', {
        'post': post,
        'comment_form': comment_form,
        'comments': comments
    })


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)

    else:
        form = PostForm()
    return render(request, 'blog/post/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post/post_edit.html', {
        'form': form,
        'post': post
    })


def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True)\
                .order_by('created_date')
    return render(request, 'blog/post/post_draft_list.html', {
        'posts': posts
    })


def post_share(request, pk):
    # Retrieve post by id
    post = get_object_or_404(Post, pk=pk)
    sent = False
    if request.method == "POST":
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            # ... send email
            post_url = request.build_absolute_uri(
                post.get_absolute_url()
            )
            subject = '{} ({}) recommends you reading "{}"'.format(
                    cd['name'],
                    cd['email'],
                    post.title)
            message = 'Read "{0}" at {1}\n\n{2}\'s comments:{3}'.format(
                        post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'admin@myblog.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {
        'post': post,
        'form': form,
        'sent': sent
    })
