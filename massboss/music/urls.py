from .import views
from django.urls import path

urlpatterns = [
    path('', views.index,name='music-index'),
    path('about/', views.about,name='music-about'),
    path('artist/', views.artist,name='music-artist'),
    path('inner-page/', views.inner,name='music-inner'),
    path('portfolio/', views.portfolio,name='music-portfolio'),
    path('track/', views.track,name='music-track'),
]