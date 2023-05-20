from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    return render(request,'music/index.html')

def tracks(request):
    items = Song.objects.all()

    context = {
        'items':items,
    }
    return render(request,'music/tracks.html',context)
    
def about(request):
    return render(request,'music/aboutus.html')


def artist(request):
    return render(request,'music/artist.html')


def videos(request):
    return render(request,'music/videos.html')

def gallery(request):
    items = Song.objects.all()

    context = {
        'items':items,
    }
    return render(request,'music/gallery.html',context)
    

@login_required
def upload(request):
    if request.method == 'POST':
        form = MusicUploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('music-tracks')
    else:
        form = MusicUploadForm()

    context = {
        'form':form,
    }
    return render(request,'music/upload.html',context)
    
