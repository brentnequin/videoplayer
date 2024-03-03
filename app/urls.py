from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new-video', views.new_video, name='new-video'),
    path('upload-video', views.upload, name='upload-video'),
]