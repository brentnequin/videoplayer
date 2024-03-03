from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import TemporaryUploadedFile

from app.apps import Config


@deconstructible
class FileSizeValidator:

    message = _(
        "File size “%(size)s” is too large. "
        "Max file size is: “%(max_size)s”."
    )
    code = "invalid_file_size"

    def __init__(self, max_size: int = None, message: str = None, code: str = None):

        self.max_size = max_size or Config.max_upload_size
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value: TemporaryUploadedFile):

        if value.size > self.max_size:

            raise ValidationError(
                    self.message,
                    code=self.code,
                    params={
                        "size": value,
                        "max_size": self.max_size,
                    },
                )
    
    def __eq__(self, other):
        return (
            isinstance(other, self.__class__)
            and self.max_size == other.max_size
            and self.message == other.message
            and self.code == other.code
        )
