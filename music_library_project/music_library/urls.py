from django.urls import path
from . import views


urlpatterns = [
    path('music_library/', views.SongList.as_view()),
    path('music_library/<int:pk>/', views.SongDetail.as_view()),
    path('music_library/like/<int:pk>/', views.LikeSong.as_view()),
]