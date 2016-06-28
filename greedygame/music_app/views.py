from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, View, UpdateView
from music_app.models import MusicTrack, MusicGenre, MusicTrackGenre
from music_app.forms import MusicTrackForm, MusicGenreForm,MusicTrackUpdateForm
from django.views.decorators.csrf import *


class MusicTrackList(ListView):
    template_name = 'music_app/templates/musictrack_list.html'
    queryset = MusicTrack.objects.order_by('title')
    context_object_name = 'musictracks_list'
    model = MusicTrack
    paginate_by = 3

    def get_queryset(self):
        print(self.request.GET.copy(), "sdsdds")

        try:
            name = self.request.GET.copy()['searchbox']
            print("sdasd")
        except:
            name = ''
        print(name, "name")
        if (name != ''):
            object_list = self.model.objects.filter(title__icontains=name)
        else:
            object_list = self.model.objects.all();
        return object_list;


class MusicGenreListForm(View):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(MusicGenreListForm, self).dispatch(*args, **kwargs)

    def get(self, request):
        form = MusicGenreForm()
        data = {'form': form}
        return render(request, 'music_app/templates/musicgenre_form.html', data)

    def post(self, request):
        print(request.POST, "12345678")
        form = MusicGenreForm(request.POST)
        if form.is_valid():
            x = form.cleaned_data
            MusicsGenre = MusicGenre(x['title'])
            MusicsGenre.save()
            return redirect("/music/genres")
        else:
            form = MusicGenreForm()
            data = {'form': form}
            return render(request, 'music_app/templates/musicgenre_form.html', data)


class MusicTrackListForm(View):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(MusicTrackListForm, self).dispatch(*args, **kwargs)

    def get(self, request):
        form = MusicTrackForm()
        data = {'form': form}
        return render(request, 'music_app/templates/musictrack_form.html', data)

    def post(self, request):
        print(request.POST, "12345678")
        form = MusicTrackForm(request.POST)
        # form.save()
        if form.is_valid():
            x = form.cleaned_data
            MusicsTrack = MusicTrack(x['title'], x['rating'])
            MusicsTrack.save()
            for genreds in x['genre'].values():
                print(x['genre'].values(), "suryaa")
                id = int(genreds['genre_id'])
                music_genre_object = MusicGenre.objects.get(genre_id=id)
                # print(qw)
                print(MusicsTrack)
                genretrack = MusicTrackGenre(track_id=MusicsTrack, genre_id=music_genre_object)
                genretrack.save()
                return redirect("/music/tracks")
        else:
            form = MusicTrackForm()
            data = {'form': form}
            return render(request, 'music_app/templates/musictrack_form.html', data)


class MusicTrackDetail(DetailView):
    template_name = 'music_app/templates/musictrack_detail.html'
    model = MusicTrack

    def get_context_data(self, **kwargs):
        context = super(MusicTrackDetail, self).get_context_data(**kwargs)
        model = MusicTrack.objects.get(pk=self.kwargs['pk'])
        print(model.track_id, "model")
        music_track_genre_object = MusicTrackGenre.objects.filter(track_id=model.track_id)
        track_list = []
        for i in music_track_genre_object:
            print(MusicGenre.objects.get(genre_id=i.genre_id_id).genre_name)
            track_list.append(MusicGenre.objects.filter(genre_id=i.genre_id_id))
        # print(music_track_genre_object.genre_id, "genre_id")
        # context['Genre'] = MusicGenre.objects.filter(MusicTrackGenre.objects.get(MusicTrack.objects.get(track_id =self.request.GET.get('pk'))).values_list('genre_id'))
        # context['Genre'] = self.object.filter(get_query(self.request.GET['q'],['genre_id', 'track_id']))
        print(track_list)
        context['Genre'] = track_list
        print(context)
        return context


class MusicGenreList(ListView):
    template_name = 'music_app/templates/musicgenre_list.html'
    queryset = MusicGenre.objects.order_by('genre_name')
    context_object_name = 'musicgenres_list'
    model = MusicGenre
    print("hiii")

    def get_queryset(self):
        print(self.request.GET.copy(), "sdsdds")

        try:
            name = self.request.GET.copy()['search']
            print("sdasd")
        except:
            name = ''
        print(name, "name")
        if (name != ''):
            object_list = self.model.objects.filter(genre_name__icontains=name)
        else:
            object_list = self.model.objects.all();
        return object_list;




# class MusicTrackUpdate(View):
    # model = MusicTrack
    # fields = ["title","rating"]
    # success_url = '/music/tracks/'

    # def get(self, request, track_id = None):
    #     e = request.GET.copy()
    #     print(e,"sisisi")
    #     music = MusicTrack.objects.get(track_id =track_id)
    #     genreId = MusicTrackGenre.objects.filter(track_id = e["track_id"])
    #     form = MusicTrackForm(title = music.title,rating = music.rating, genre = genreId)
    #     data = {'form': form}
    #     return render(request, 'music_app/templates/musictrack_update.html', data)

    # template_name = 'music_app/templates/musictrack_update.html'

class MusicGenreDetail(DetailView):
    template_name = 'music_app/templates/musicgenre_detail.html'
    model = MusicGenre

    def get_context_data(self, **kwargs):
        context = super(MusicGenreDetail, self).get_context_data(**kwargs)
        model = MusicGenre.objects.get(pk=self.kwargs['pk'])
        print(model.genre_id, "model")
        music_track_genre_object = MusicTrackGenre.objects.filter(genre_id=model.genre_id)
        track_list = []
        for i in music_track_genre_object:
              print(i.track_id_id,"track_id")
        #     print(MusicTrack.objects.get(track_id=i.track_id_id).title)
              track_list.append(MusicTrack.objects.filter(track_id=i.track_id_id))
        # print(track_list)
        context['Track'] = track_list
        print(context,"context")
        return context