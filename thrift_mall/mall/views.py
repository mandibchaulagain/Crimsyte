from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def index(request):
    # Create a range for the gallery images (16 images)
    gallery_range = [str(i) for i in range(1, 17)]
    return render(request, 'mall/index.html', {'gallery_range': gallery_range})