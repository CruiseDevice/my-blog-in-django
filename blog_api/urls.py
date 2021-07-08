from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('posts/', views.PostListView.as_view()),
    path('post/<int:pk>/', views.PostDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)