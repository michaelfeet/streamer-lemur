
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Media, Journal, Photo

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

import uuid
import boto3


# session = boto3.Session(profile_name='streamerlemurbucket1')
# streamerlemurbucket1_s3_client = session.client('s3')

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'streamerlemurbucket1'

def home(request):
    return render(request, 'home.html')


class MediaCreate(LoginRequiredMixin, CreateView):
    model = Media
    fields = '__all__'


class MediaList(ListView):
    model = Media


class MediaDetail(DetailView):
    model = Media
    
    def journal_exist(self):
        media = Media.objects.get(id=self.kwargs['pk'])
        # is we need to identify if a journal exists, using both the media object and the user object
        # first grab all journals with associated with that media
        journal_list = Journal.objects.filter(media=media)
        # then take that list and see if any have the same user id
        journal = journal_list.objects.filter(user=self.request.user)
        return render(super(), {'journal': journal})


class JournalCreate(LoginRequiredMixin, CreateView):
    model = Journal
    fields = ['last_date_watched', 'continue_watching',
              'completed_watching', 'would_watch_again',
              'where_am_i_watching', 'last_episode_watched']

    def form_valid(self, form):
        media = Media.objects.get(id=self.kwargs['media_id'])
        form.instance.user = self.request.user
        form.instance.media = media
        return super().form_valid(form)


@login_required
def journal_list(request):
    journal_list = Journal.objects.filter(user=request.user)
    return render(request, 'main_app/journal_list.html', {'journal_list': journal_list})


@login_required
def journal_detail(request, journal_id):
    journal = Journal.objects.get(id=journal_id)
    media = Media.objects.get(id=journal.media.id)

    return render(request, 'main_app/journal_detail.html', {'journal': journal, 'media': media})


class JournalUpdate(LoginRequiredMixin, UpdateView):
    model = Journal
    fields = ['last_date_watched', 'continue_watching',
              'completed_watching', 'would_watch_again',
              'where_am_i_watching', 'last_episode_watched']


class JournalDelete(LoginRequiredMixin, DeleteView):
    model = Journal
    success_url = '/journals/'


def signup(request):
    error_message = 'this was so easy, how'
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'this was so easy, how'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


@login_required
def add_photo(request, media_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + \
            photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            Photo.objects.create(url=url, media_id=media_id)
        except:
            print('An error occurred uploading file to S3')
    return redirect('media_detail', pk=media_id)
