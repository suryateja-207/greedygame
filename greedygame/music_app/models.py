from django.db import models
# from django import forms
from django.forms import ModelForm
class MusicTrack(models.Model):
    title = models.CharField(unique=True, max_length=40)
    rating = models.IntegerField()
    track_id = models.AutoField(primary_key=True)

    class Meta:
        verbose_name = "MusicTrack"
        verbose_name_plural = "MusicTrack"

#
# class MusicTrackForm(ModelForm):
#     class Meta:
#         model = MusicTrack
#         fields = ["title","rating"]

# class MusicTrackForm(forms.Form):
#     title = forms.CharField(max_length=40)
#     rating = forms.IntegerField()
#     genre = forms.ModelMultipleChoiceField(queryset = MusicGenre.objects.all())

class MusicGenre(models.Model):
    genre_name = models.CharField(unique=True, max_length=40)
    genre_id = models.AutoField(primary_key=True)
#
# class MusicGenreForm(ModelForm):
#     class Meta:
#         model = MusicGenre
#         fields = ["genre_name"]

class MusicTrackGenre(models.Model):
    track_id = models.ForeignKey(MusicTrack,on_delete=models.CASCADE)
    genre_id = models.ForeignKey(MusicGenre, on_delete=models.CASCADE)

    # def __str__(self):
    #     return "(%s) %s" % (self.track_id, self.genre_id)

