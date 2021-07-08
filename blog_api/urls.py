from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('posts/', views.post_list),
    url(r'^posts/tag/(?P<tag_slug>[-\w]+)/$', views.post_list),
    path('post/<int:pk>/', views.post_detail),
    path('drafts/', views.post_draft),
]

urlpatterns = format_suffix_patterns(urlpatterns)