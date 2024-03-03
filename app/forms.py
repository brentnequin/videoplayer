from typing import Any
from django import forms
from django.core.validators import FileExtensionValidator
from app.validators import FileSizeValidator


class UploadVideoForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField(validators=[FileExtensionValidator(allowed_extensions=['mp4']), FileSizeValidator(max_size=1024*1024*4)])
