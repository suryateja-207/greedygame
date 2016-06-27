from django.shortcuts import render
from django.views.generic import ListView, DetailView,View
from music_app.models import MusicTrack, MusicGenre, MusicTrackGenre
from music_app.forms import MusicTrackForm
from django.views.decorators.csrf import *


class MusicTrackList(ListView):
    template_name = 'music_app/templates/musictrack_list.html'
    queryset = MusicTrack.objects.order_by('title')
    context_object_name = 'musictracks_list'
    model = MusicTrack
    paginate_by = 2

class MusicTrackListForm(View):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(MusicTrackListForm, self).dispatch(*args, **kwargs)
    def get(self,request):
        form = MusicTrackForm()
        data = {'form':form}
        return render(request, 'music_app/templates/musictrack_form.html',data)
    def post(self,request):
        print(request.POST,"12345678")
        form = MusicTrackForm(request.POST)
        # form.save()
        if form.is_valid():
            print("rfff")
            x = form.cleaned_data
            MusicsTrack = MusicTrack(x['title'],x['rating'])
            MusicsTrack.save()
            for genreds in x['genre'].values():
                ids = int(genreds['genre_id'])
                qw = MusicGenre.objects.get(genre_id=ids)
                # print(qw)
                print(MusicsTrack)
                genretrack = MusicTrackGenre(track_id = MusicsTrack, genre_id= qw )
                genretrack.save()

        else:
            form = MusicTrackForm()
            data = {'form': form}
            return render(request, 'music_app/templates/musictrack_form.html', data)



class MusicTrackDetail(DetailView):
    template_name = 'music_app/templates/musictrack_detail.html'
    model = MusicTrack
    # def get_object(self):
    #     model = MusicTrack.objects.get(pk=self.kwargs['pk'])
    #     print(model.track_id,"model")
    def get_context_data(self, **kwargs):
        context = super(MusicTrackDetail, self).get_context_data(**kwargs)
        model = MusicTrack.objects.get(pk=self.kwargs['pk'])
        print(model.track_id, "model")
        music_track_genre_object = MusicTrackGenre.objects.filter(track_id = model.track_id)
        for i in music_track_genre_object:
            # print(i.genre_id_id,"genre_id")
            print(MusicGenre.objects.get(genre_id = i.genre_id_id).genre_name)
            context['Genre'] = MusicGenre.objects.filter(genre_id = i.genre_id_id)
            print(context,"length")
        # print(music_track_genre_object.genre_id, "genre_id")
        # context['Genre'] = MusicGenre.objects.filter(MusicTrackGenre.objects.get(MusicTrack.objects.get(track_id =self.request.GET.get('pk'))).values_list('genre_id'))
        # context['Genre'] = self.object.filter(get_query(self.request.GET['q'],['genre_id', 'track_id']))

        return context


class MusicGenreList(ListView):
    template_name = 'music_app/templates/musicgenre_list.html'
    queryset = MusicGenre.objects.order_by('genre_name')
    context_object_name = 'musicgenres_list'
    model = MusicGenre


class MusicGenreDetail(DetailView):
    template_name = 'music_app/templates/musicgenre_detail.html'
    model = MusicGenre
