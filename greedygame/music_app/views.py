from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, View, UpdateView
from music_app.models import MusicTrack, MusicGenre, MusicTrackGenre
from music_app.forms import MusicTrackForm, MusicGenreForm,MusicTrackUpdateForm
from django.views.decorators.csrf import *

'''Display all the tracks in a page'''
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

'''When you click on a single track It will show the details of the song'''
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
        print(track_list)
        context['Genre'] = track_list
        print(context)
        return context

'''Adding a new track with its details like rating and genrename'''
class MusicTrackListForm(View):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(MusicTrackListForm, self).dispatch(*args, **kwargs)

    def get(self, request):
        form = MusicTrackForm()
        data = {'form': form}
        return render(request, 'music_app/templates/musictrack_form.html', data)

    def post(self, request):
        print(request.POST)
        form = MusicTrackForm(request.POST)
        if form.is_valid():
            x = form.cleaned_data
            music_track = MusicTrack(x['title'], x['rating'])
            music_track.save()
            for genres in x['genre'].values():
                id = int(genres['genre_id'])
                music_genre_object = MusicGenre.objects.get(genre_id=id)
                print(music_track)
                genre_track = MusicTrackGenre(track_id=music_track, genre_id=music_genre_object)
                genre_track.save()
                return redirect("/music/tracks")
        else:
            form = MusicTrackForm()
            data = {'form': form}
            return render(request, 'music_app/templates/musictrack_form.html', data)

'''Display all the genres in a page'''
class MusicGenreList(ListView):
    template_name = 'music_app/templates/musicgenre_list.html'
    queryset = MusicGenre.objects.order_by('genre_name')
    context_object_name = 'musicgenres_list'
    model = MusicGenre

    def get_queryset(self):
        try:
            name = self.request.GET.copy()['search']
        except:
            name = ''
        if (name != ''):
            object_list = self.model.objects.filter(genre_name__icontains=name)
        else:
            object_list = self.model.objects.all()
        return object_list;

'''Whenever a user clicks on genre it will display all the songs related to that genre.'''
class MusicGenreDetail(DetailView):
    template_name = 'music_app/templates/musicgenre_detail.html'
    model = MusicGenre

    def get_context_data(self, **kwargs):
        context = super(MusicGenreDetail, self).get_context_data(**kwargs)
        model = MusicGenre.objects.get(pk=self.kwargs['pk'])
        music_track_genre_object = MusicTrackGenre.objects.filter(genre_id=model.genre_id)
        track_list = []
        for i in music_track_genre_object:
              track_list.append(MusicTrack.objects.filter(track_id=i.track_id_id))
        context['Track'] = track_list
        print(context,"context")
        return context

'''Adding a new genre'''
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
            music_genre = MusicGenre(x['title'])
            music_genre.save()
            return redirect("/music/genres")
        else:
            form = MusicGenreForm()
            data = {'form': form}
            return render(request, 'music_app/templates/musicgenre_form.html', data)

'''updating the music track'''
class MusicTrackUpdate(UpdateView):
    model = MusicTrack
    fields = ["title","rating"]
    success_url = '/music/tracks/'
    template_name = 'music_app/templates/musictrack_update.html'

'''updating the genre name'''
class MusicGenreUpdate(UpdateView):
    model = MusicGenre
    fields = ["genre_name"]
    success_url = '/music/genres/'
    template_name = 'music_app/templates/musicgenre_update.html'

