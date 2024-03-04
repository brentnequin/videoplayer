from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from app.models import Video
from app.forms import UploadVideoForm
from django.views.decorators.http import require_http_methods

def index(request: HttpRequest):

    return render(
        request, 'index.html',
        context={
            'videos': Video.objects.order_by('-date')
        }
    )


@require_http_methods(["GET", "POST"])
def upload(request: HttpRequest):

    if request.method == 'GET':
        return render(request, 'upload.html')
    
    elif request.method == 'POST':
        form = UploadVideoForm(data=request.POST or None, files=request.FILES)

        if not form.is_valid():
            return HttpResponse(
                f'<p class="error">Your form submission was unsuccessful ❌. Please would you correct the errors? The current errors: {form.errors}</p>')

        video = Video(**form.cleaned_data, owner=request.user)
        video.save()
        return HttpResponse('Success')  


def watch(request: HttpRequest):

    if not (video_id := request.GET.get('v')):
        return redirect('index')

    return render(request, 'watch.html', {
        'video': Video.objects.get(id=video_id)
    })
