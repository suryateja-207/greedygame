from django.conf.urls import url
from music_app.views import MusicTrackList, MusicTrackDetail, MusicGenreList, MusicGenreDetail, MusicTrackListForm, MusicGenreListForm,MusicTrackUpdate,MusicGenreUpdate

urlpatterns = [
    url(r'^tracks/addtrack/$', MusicTrackListForm.as_view()),
    url(r'^genres/addgenre/$', MusicGenreListForm.as_view()),
    url(r'^tracks/$', MusicTrackList.as_view()),
    url(r'^tracks/edit/(?P<pk>[0-9]+)/$', MusicTrackUpdate.as_view()),
    url(r'^tracks/(?P<pk>[-\w]+)/$',MusicTrackDetail.as_view()),
    url(r'^genres/$',MusicGenreList.as_view()),
    url(r'^genres/(?P<pk>[-\w]+)/$',MusicGenreDetail.as_view()),
    url(r'^genres/edit/(?P<pk>[0-9]+)/$', MusicGenreUpdate.as_view()),

]