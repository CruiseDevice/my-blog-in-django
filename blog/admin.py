# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post, Comment, Tag
# Register your models here.


class TagInline(admin.TabularInline):
    model = Post.tags.through


class CommentInline(admin.TabularInline):
    model = Comment

class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'author', 'published_date', 'status')
    list_filter = ('status', 'created_date', 'published_date', 'author')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'published_date'
    ordering = ['status', 'published_date']

    inlines = [
        TagInline,
        CommentInline
    ]


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag)