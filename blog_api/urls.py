from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list),
    url(r'post/(?P<pk>\d+)/$', views.post_detail),
    url(r'drafts/$', views.post_draft),
]
