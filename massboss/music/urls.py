from .import views
from django.urls import path

urlpatterns = [
    path('', views.index,name='music-index'),
    path('tracks/', views.tracks,name='music-tracks'),
    path('about/', views.about,name='music-about'),
    path('artist/', views.artist,name='music-artist'),
    path('videos/', views.videos,name='music-videos'),
    path('gallery/', views.gallery,name='music-gallery'),
    path('upload/', views.upload,name='music-upload'),
]