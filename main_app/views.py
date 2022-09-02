
from django.shortcuts import render
from django.http import HttpResponse

from .models import Media

from django.views.generic.edit import CreateView


# Create your views here.
def home(request):
    return render(request, 'home.html')

class MediaCreate(CreateView):
    model=Media
    fields = '__all__'