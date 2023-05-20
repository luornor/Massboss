from django import forms
from .models import *

class MusicUploadForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title','artist','genre','producer','image','song']



