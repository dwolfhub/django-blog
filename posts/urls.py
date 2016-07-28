from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='list'),
    url(r'^(?P<slug>[a-z0-9\-]+)$', views.single, name='single'),
    url(r'^author/(?P<username>[a-z]+)$', views.author, name='author'),
]