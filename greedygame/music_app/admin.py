from django.contrib import admin
from music_app import models

# Register your models here.
class MusicTrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'rating', 'track_id')
    list_filter = ('title', 'rating', 'track_id')

class MusicGenreAdmin(admin.ModelAdmin):
    list_display = ('genre_name', 'genre_id')

class MusicTrackGenreAdmin(admin.ModelAdmin):
    list_display = ('track_id', 'genre_id')



admin.site.register(models.MusicTrack, MusicTrackAdmin)
admin.site.register(models.MusicGenre, MusicGenreAdmin)
admin.site.register(models.MusicTrackGenre, MusicTrackGenreAdmin)
