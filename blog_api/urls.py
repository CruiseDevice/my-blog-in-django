from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list),
]
