from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from app.models import Video
from app.forms import UploadVideoForm

def index(request: HttpRequest):
    data = {
        'videos': Video.objects.order_by('-date')
    }
    return render(request, 'index.html', context=data)

def new_video(request: HttpRequest):
    return render(request, 'new-video.html')

def upload(request: HttpRequest):  
    form = UploadVideoForm(data=request.POST or None, files=request.FILES)

    if not form.is_valid():
        return HttpResponse(
            f'<p class="error">Your form submission was unsuccessful ❌. Please would you correct the errors? The current errors: {form.errors}</p>')

    video = Video(**form.cleaned_data, owner=request.user)
    video.save()
    return HttpResponse('Success')  
