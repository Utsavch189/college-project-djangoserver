from django.urls import path
from micro_music_service.controller.playlist_views import Playlist

urlpatterns = [
    path('playlist/userid=<str:userid>',Playlist.as_view())
]
