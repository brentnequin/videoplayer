from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import login as login_user, logout as logout_user

from authlib.integrations.django_client import OAuth, OAuthError

from urllib.parse import quote_plus, urlencode

from app.models import Video
from app.forms import UploadVideoForm

oauth = OAuth()

oauth.register(
    "auth0",
    client_id=settings.AUTH0_CLIENT_ID,
    client_secret=settings.AUTH0_CLIENT_SECRET,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
)

def login(request: HttpRequest):
    return oauth.auth0.authorize_redirect(
        request, request.build_absolute_uri(reverse("callback"))
    )

def callback(request: HttpRequest):
    try:
        token = oauth.auth0.authorize_access_token(request)
        request.session["user"] = token
        user = User.objects.get(email__exact=token['userinfo']['email'])
    except OAuthError:
        return redirect(request.build_absolute_uri(reverse("index")))
    except User.DoesNotExist:
        user = User.objects.create(
            username=token['userinfo']['nickname'],
            email=token['userinfo']['email'],
            password=""
        )

    login_user(request, user)
    return redirect(request.build_absolute_uri(reverse("index")))

def logout(request: HttpRequest):

    logout_user(request)
    request.session.clear()

    return redirect(
        f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
        + urlencode(
            {
                "returnTo": request.build_absolute_uri(reverse("index")),
                "client_id": settings.AUTH0_CLIENT_ID,
            },
            quote_via=quote_plus,
        ),
    )

def _common_context(request: HttpRequest):
    return {
        'session': request.session.get('user')
    }

def index(request: HttpRequest):

    return render(
        request, 'index.html',
        context=_common_context(request) | {
            'videos': Video.objects.order_by('-date'),
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
        response = HttpResponse()
        response["HX-Redirect"] = f'/watch?v={str(video.id)}'
        return response


def watch(request: HttpRequest):

    if not (video_id := request.GET.get('v')):
        return redirect('index')

    if not (video := Video.objects.get(id=video_id)):
        return redirect('index')

    video.views += 1
    video.save()

    return render(request, 'watch.html', {
        'video': video
    })
