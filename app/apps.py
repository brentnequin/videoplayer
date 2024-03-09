from django.apps import AppConfig
import cloudinary
from videoplayer import settings


MAX_UPLOAD_SIZE = 1024 * 1024 * 4


class Config(AppConfig):
    name = 'app'

    max_upload_size = MAX_UPLOAD_SIZE

    cloudinary.config( 
        cloud_name = settings.CLOUDINARY_NAME,
        api_key = settings.CLOUDINARY_API_KEY,
        api_secret = settings.CLOUDINARY_API_SECRET,
        secure=True
    )
