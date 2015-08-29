from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^newstory$', views.newstory, name='newstory'),
  url(r'^write$', views.write, name='write'),
  url(r'^about$', views.about, name='about'),
  url(r'^(?P<story_id>[0-9]+)/$', views.detail, name='detail'),
]
