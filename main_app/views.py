
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Media, Journal

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def home(request):
    return render(request, 'home.html')


class MediaCreate(CreateView):
    model = Media
    fields = '__all__'


class MediaList(ListView):
    model = Media


class MediaDetail(DetailView):
    model = Media


class JournalCreate(LoginRequiredMixin, CreateView):
    model = Journal
    fields = ['last_date_watched', 'continue_watching',
              'completed_watching', 'would_watch_again', 'movie']

    def form_valid(self, form):
        media = Media.objects.get(id=self.kwargs['media_id'])
        form.instance.user = self.request.user
        form.instance.media = media
        return super().form_valid(form)


def journal_list(request):
    journal_list = Journal.objects.filter(user=request.user)
    return render(request, 'main_app/journal_list.html', {'journal_list': journal_list})


def journal_detail(request, journal_id):
    journal = Journal.objects.get(id=journal_id)
    media = Media.objects.get(id=journal.media.id)

    return render(request, 'main_app/journal_detail.html', {'journal': journal, 'media': media})


class JournalUpdate(UpdateView):
    model = Journal
    fields = ['last_date_watched', 'continue_watching',
              'completed_watching', 'would_watch_again', 'movie']


class JournalDelete(DeleteView):
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
