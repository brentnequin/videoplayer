from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload', views.upload, name='upload'),
    path('watch', views.watch, name='watch'),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("callback", views.callback, name="callback"),
]