from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<post_pk>\d+)/comments/new/$', views.comment_new, name='comment_new'),
]

