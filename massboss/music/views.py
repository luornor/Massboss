from django.shortcuts import render,redirect
from .forms import *
from django.core.mail import send_mail

  

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            submitted = False
            subject = "Website Inquiry" 
            body = {
            'name': form.cleaned_data['name'], 
            'email': form.cleaned_data['email'], 
            'message':form.cleaned_data['message'], 
            }
            
            message = f"\n Name: {body['name']} \n E-mail: {body['email']} \n Message: {body['message']} "
            send_mail(subject, message,from_email=body['email'],recipient_list=['jamesmacgyver442@gmail.com'])
            return redirect('music-index')
    else:
        form = ContactForm()
    context = {
        'form': form,
    }

    return render(request,'music/index.html', context)
    
def about(request):
    return render(request,'music/aboutus.html')


def artist(request):
    return render(request,'music/artist.html')


def inner(request):
    return render(request,'music/inner-page.html')


def portfolio(request):
    return render(request,'music/portfolio-details.html')

def track(request):
    return render(request,'music/track.html')
    
