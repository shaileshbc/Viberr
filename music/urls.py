from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    
    url(r'^(?P<pk>[0-9]+)/$', views.AlbumDetail.as_view(), name='detail'),
    url(r'^create_album/$', views.AlbumCreate.as_view(), name='create_album'),
    url(r'^album/(?P<pk>[0-9]+)$', views.AlbumUpdate.as_view(), name='update_album'),
    url(r'^(?P<album_id>[0-9]+)/delete_album/$', views.AlbumDelete.as_view(), name='delete_album'),
    
    url(r'^(?P<album_id>[0-9]+)/create_song/$', views.create_song, name='create_song'),
    url(r'^songs/(?P<filter_by>[a-zA_Z]+)/$', views.songs, name='songs'),
    url(r'^(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),
    
]
