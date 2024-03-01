from django.urls import path
from . import views

urlpatterns = [
    # frontend routes
    path('', views.index, name='index')
]