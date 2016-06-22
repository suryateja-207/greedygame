from django.shortcuts import render
from django.views.generic import ListView, DetailView
from music_app.models import MusicTrack, MusicGenre, MusicTrackGenre


class MusicTrackList(ListView):
    template_name = 'music_app/templates/musictrack_list.html'
    queryset = MusicTrack.objects.order_by('title')
    context_object_name = 'musictracks_list'
    model = MusicTrack
    paginate_by = 2


class MusicTrackDetail(DetailView):
    template_name = 'music_app/templates/musictrack_detail.html'
    model = MusicTrack
    def get_context_data(self, **kwargs):
        context = super(MusicTrackDetail, self).get_context_data(**kwargs)
        print(pk)
        # context['Genre'] = MusicGenre.objects.filter(MusicTrackGenre.objects.get(MusicTrack.objects.get(track_id =self.request.GET.get('pk'))).values_list('genre_id'))
        context['Genre'] = self.object.applied_to.filter(get_query(self.request.GET['q'],/
        ['genre_id', 'track_id']))
        return context


class MusicGenreList(ListView):
    template_name = 'music_app/templates/musicgenre_list.html'
    queryset = MusicGenre.objects.order_by('genre_name')
    context_object_name = 'musicgenres_list'
    model = MusicGenre


class MusicGenreDetail(DetailView):
    template_name = 'music_app/templates/musicgenre_detail.html'
    model = MusicGenre
