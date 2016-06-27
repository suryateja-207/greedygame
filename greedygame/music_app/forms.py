from django import forms
from music_app.models import MusicTrack,MusicGenre,MusicTrackGenre
class MusicTrackForm(forms.Form):
    title = forms.CharField(max_length=40)
    rating = forms.IntegerField()
    genre = forms.ModelMultipleChoiceField(queryset = MusicGenre.objects.all())

class MusicGenreForm(forms.Form):
    title = forms.CharField(max_length=40)

class MusicTrackUpdateForm(forms.ModelForm):
    class Meta:
        title = forms.CharField(max_length=40)
        rating = forms.IntegerField()
        genre = forms.ModelMultipleChoiceField(queryset=MusicGenre.objects.all())