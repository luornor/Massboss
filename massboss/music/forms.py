from django import forms
from .models import *

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255,required=True,widget=forms.TextInput(attrs={'placeholder': 'Your name'}))
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Your Email'}))
    message = forms.CharField(required=True,widget=forms.Textarea(attrs={'rows':5,'placeholder': 'Your message'})
                            )
    