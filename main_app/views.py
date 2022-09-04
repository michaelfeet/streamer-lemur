
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
    fields = ['last_date_watched', 'continue_watching', 'completed_watching', 'would_watch_again', 'movie']
    
    
    def form_valid(self, form):
        media = Media.objects.get(id= self.kwargs['media_id'])
        form.instance.user = self.request.user
        form.instance.media = media
        return super().form_valid(form)
    
class JournalList(ListView):
    model=Journal

class JournalDetail(DetailView):
    model=Journal