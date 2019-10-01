from django.conf.urls import url
from . import views

# app_name='blog'
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$',
        views.post_list, name='post_list_by_tag'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/share/$', views.post_share, name='post_share'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/share/$', views.post_share, name='post_share'),
]
