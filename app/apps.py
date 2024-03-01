from django.apps import AppConfig
import cloudinary


class Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    cloudinary.config( 
        cloud_name = "dpazoxrkf", 
        api_key = "884621821116849", 
        api_secret = "dN931d1JUd7Do2_9-fToBx5Gx38" 
    )