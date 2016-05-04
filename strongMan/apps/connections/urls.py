from django.conf.urls import url

from . import views

app_name = 'connections'
urlpatterns = [
    url(r'^$', views.overview, name='index'),
    url(r'^add/$', views.create, name='connections_choose'),
    url(r'^(?P<id>\d+)/$', views.update, name='connection_update'),
    url(r'delete/(?P<id>\d+)/$', views.delete_connection, name='connection_delete'),
    url(r'state/(?P<id>\d+)/$', views.get_state, name='connection_state'),
    url(r'log/$', views.get_log, name='connection_log'),
    url(r'toggle/$', views.toggle_connection, name='connection_toggle'),
    url(r'info/$', views.get_sa_info, name='connection_info'),
]
