from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.post_list),
	url(r'^details/(?P<post_id>[0-9]+)/$', views.post_detail),
	url(r'^details/(?P<post_id>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^details/(?P<post_id>[0-9]+)/publish/$', views.post_publish, name='post_publish'),
	url(r'^post/(?P<post_id>[0-9]+)/delete/$', views.post_delete, name='post_delete'),
	url(r'^post/publish/$', views.post_unpublished, name='post_unpublished'),
	url(r'^post/new/$', views.post_new, name='post_new'),
]