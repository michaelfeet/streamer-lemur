from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('media/create', views.MediaCreate.as_view(), name='media_create'),
    path('media/', views.MediaList.as_view(), name='media_index'),
    path('media/<int:pk>', views.MediaDetail.as_view(), name='media_detail'),
    path('media/<int:media_id>/journal/create', views.JournalCreate.as_view(), name='journal_create'),
    path('journals/', views.journal_list, name='journals_index'),
    path('journals/<int:journal_id>', views.journal_detail, name='journals_detail'),
    path('journals/<int:pk>/update/', views.JournalUpdate.as_view(), name='journals_update'),
    path('journals/<int:pk>/delete/', views.JournalDelete.as_view(), name='journals_delete'),
    path('accounts/signup/', views.signup, name='signup')
]