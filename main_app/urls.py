from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('media/create', views.MediaCreate.as_view(), name='media_create')
]
