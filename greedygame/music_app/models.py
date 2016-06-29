from django.db import models
class MusicTrack(models.Model):
    title = models.CharField(unique=True, max_length=40)
    rating = models.IntegerField()
    track_id = models.AutoField(primary_key=True)

    class Meta:
        verbose_name = "MusicTrack"
        verbose_name_plural = "MusicTrack"

class MusicGenre(models.Model):
    genre_name = models.CharField(unique=True, max_length=40)
    genre_id = models.AutoField(primary_key=True)
    def __str__(self):
        return "%s" % (self.genre_name)


class MusicTrackGenre(models.Model):
    track_id = models.ForeignKey(MusicTrack,on_delete=models.CASCADE)
    genre_id = models.ForeignKey(MusicGenre, on_delete=models.CASCADE)