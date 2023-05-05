from django.shortcuts import render
from django.http import HttpResponse
import whisper
import pyaudio
# Create your views here.

def home(request):
    return render (request, 'index.html')