from django.db import models
from django.contrib.auth.models import User
import random
import string
from datetime import date
from cloudinary.models import CloudinaryField


def generate_unique_id():
    length = 10
    while True:
        id = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=length))
        if Video.objects.filter(id=id).count() == 0:
            break
    return id


class Video(models.Model):
    id = models.CharField(max_length=10, default=generate_unique_id, unique=True, primary_key=True)
    video = CloudinaryField(id, resource_type='video', folder='video-player')
    # thumbnail = models.FileField(upload_to='', blank=True)
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=128)
    owner = models.ForeignKey(User, related_name='videos', on_delete=models.CASCADE)
    date = models.DateField(default=date.today)

    @property
    def url(self):
        return self.video.url

    @property
    def thumbnail_url(self):
        return self.video.video_thumbnail()
