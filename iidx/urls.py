from django.urls import path
from .views import GetMusicList

urlpatterns = [
    path('music-list/', GetMusicList.as_view()),
]
