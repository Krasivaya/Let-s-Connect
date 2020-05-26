from django.conf.urls import url, include
from . import views

urlpatterns=[
    url(r'^$', views.posts, name='posts'),
    url(r'^article/(\d+)', views.article, name='article'),
]