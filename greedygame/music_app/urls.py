from django.conf.urls import url
from music_app.views import MusicTrackList, MusicTrackDetail, MusicGenreList, MusicGenreDetail

urlpatterns = [
    url(r'^tracks/$', MusicTrackList.as_view()),
    url(r'^tracks/(?P<pk>[-\w]+)/$',MusicTrackDetail.as_view()),
    url(r'^genres/$',MusicGenreList.as_view()),
    url(r'^genres/(?P<pk>[-\w]+)/$',MusicGenreDetail.as_view()),

]