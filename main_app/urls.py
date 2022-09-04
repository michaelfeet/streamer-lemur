from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('media/create', views.MediaCreate.as_view(), name='media_create'),
    path('media/', views.MediaList.as_view(), name='media_index'),
    path('media/<int:pk>', views.MediaDetail.as_view(), name='media_detail'),
    path('media/<int:media_id>/journal/create', views.JournalCreate.as_view(), name='journal_create'),
    path('journals/', views.JournalList.as_view(), name='journals_index'),
    path('journals/<int:pk>', views.JournalDetail.as_view(), name='journals_detail'),
]