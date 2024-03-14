from django.db import models
from django.contrib.auth.models import User
from datetime import date
from cloudinary.models import CloudinaryField
import uuid


class Tag(models.Model):
    label = models.CharField(max_length=64)
    slug = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)


class Video(models.Model):
    id = models.CharField(max_length=36, default=uuid.uuid1, unique=True, primary_key=True)
    file = CloudinaryField(id, resource_type='video', folder='video-player')
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=128, blank=True)
    owner = models.ForeignKey(User, related_name='videos', on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    tags = models.ManyToManyField(Tag, related_name='videos')
    views = models.IntegerField(default=0)

    @property
    def url(self):
        return self.file.url

    @property
    def thumbnail_url(self):
        return self.file.video_thumbnail()
