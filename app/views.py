from django.shortcuts import render
from app.models import Video

def index(request):
    data = {
        'videos': Video.objects.order_by('-date')
    }
    return render(request, 'index.html', context=data)
