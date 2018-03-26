# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# Create your models here.

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
    )
    author = models.ForeignKey('auth.User')
    slug = models.SlugField(max_length=250,unique_for_date='published_date',default='')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null = True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    picture = models.ImageField(upload_to='post_images',blank=True)

    class Meta:
        ordering = ('-published_date',)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args = [self.published_date.year,
                                                   self.published_date.strftime('%m'),
                                                   self.published_date.strftime('%d'),
                                                   self.slug])

class Comment(models.Model):
    post    = models.ForeignKey(Post,related_name='comments')
    name    = models.CharField(max_length=180)
    email   = models.EmailField()
    body    = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active  = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name,self.post)

