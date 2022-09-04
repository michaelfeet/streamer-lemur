
from django.shortcuts import render
from django.http import HttpResponse

from .models import Media, Journal

from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView


# Create your views here.
def home(request):
    return render(request, 'home.html')

class MediaCreate(CreateView):
    model=Media
    fields = '__all__'

class MediaList(ListView):
    model=Media

class MediaDetail(DetailView):
    model=Media

class JournalCreate(CreateView):
    model = Journal
    fields = '__all__' 

def ournalCreate(request):
    pass