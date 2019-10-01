# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.staticfiles import finders


class IndexPageTests(TestCase):

    def test_index_using_template(self):
        # check the template used to render index page
        response = self.client.get(reverse('post_list'))
        self.assertTemplateUsed(response, 'blog/post/post_list.html')

    def test_index_has_heading(self):
        response = self.client.get(reverse('post_list'))
        self.assertIn(b'<h1>', response.content)
        self.assertIn(b'</h1>', response.content)


class NewPostViewTests(TestCase):

    def test_new_post_view_using_template(self):
        response = self.client.get(reverse('post_new'))
        self.assertTemplateUsed(response, 'blog/post/post_edit.html')


class PostDetailViewTests(TestCase):

    def test_post_detail_view_using_template(self):
        response = self.client.get(reverse('post_detail'))
        self.assertTemplateUsed(response, 'blog/post/post_detail.html')

    def test_post_detail_view_has_heading(self):
        response = self.client.get(reverse('post_detail'))
        self.assertIn(b'<h1>', response.content)
        self.assertIn(b'</h1>', response.content)


class PostEditViewTests(TestCase):

    def test_post_edit_view_using_template(self):
        response = self.client.get(reverse('post_edit'))
        self.assertTemplateUsed(response, 'blog/post/post_edit.html')

    def test_post_edit_view_has_heading(self):
        response = self.client.get('post_edit')
        self.assertIn(b'<h1>', response.content)
        self.assertIn(b'</h1>', response.content)


class PostShareViewTests(TestCase):

    def test_post_share_view_using_template(self):
        response = self.client.get(reverse('post_share'))
        self.assertTemplateUsed(response, 'blog/post/share.html')


class PostDraftListViewTests(TestCase):

    def test_post_draft_list_test_view_using_template(self):
        response = self.client.get(reverse('post_draft_list'))
        self.assertTemplateUsed(response, 'blog/post/post_draft_list.html')

    def test_post_draft_list_view_has_heading(self):
        response = self.client.get(reverse('post_draft_list'))
        self.assertIn(b'<h1>', response.content)
        self.assertIn(b'</h1>', response.content)

