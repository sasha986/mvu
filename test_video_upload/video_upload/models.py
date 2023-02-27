from django.db import models
from django.conf import settings

from .validators import MimetypeValidator, FileSizeValidator
from .utils import hash_video_filename, hash_thumbnail_filename

# Overwrite if the same file is uploaded two times
from django.core.files.storage import FileSystemStorage
class OverwriteStorage(FileSystemStorage):

    def get_available_name(self, name, max_length=None):
        self.delete(name)
        return name
    

# Test Measurements video model
class Video(models.Model):
    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'
        ordering = ['-id']

    title = models.CharField(max_length=250, null=False, blank=False)
    description = models.CharField(max_length=250, null=False, blank=False)
    thumbnail = models.ImageField(upload_to=hash_thumbnail_filename, null=False, blank=False, storage=OverwriteStorage())
    video = models.FileField(upload_to=hash_video_filename, null=False, blank=False, storage=OverwriteStorage())

    uploaded_dt = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='uploaded_videos', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Video, self).save(*args, **kwargs)