from django import forms
from .validators import MimetypeValidator, FileSizeValidator


# file types and file size limiations  
VIDEO_CONTENT_TYPES = ('video/mp4',) # allowed video file types
IMAGE_CONTENT_TYPES = ('image/png', 'image/jpeg', 'image/jpg',) # allowed images file types
VIDEO_FILE_SIZE_IN_BYTES = 1024 * 1024 * 10  # max allowed video file size ~10 Mib
IMAGE_FILE_SIZE_IN_BYTES = 1024 * 1024 # max allowed thumbnail file size ~1 Mb


class UploadVideoModelForm(forms.ModelForm):
    """
    UploadVideoModelForm is used to upload video and update video details
    """
    
    title = forms.CharField(max_length=250)
    description = forms.CharField(max_length=250, required=False)
    video = forms.FileField(validators=[MimetypeValidator(VIDEO_CONTENT_TYPES, code='video/mp4'), FileSizeValidator(VIDEO_FILE_SIZE_IN_BYTES)])
    thumbnail = forms.ImageField(validators=[MimetypeValidator(IMAGE_CONTENT_TYPES, code='image/png,jpeg,jpg'), FileSizeValidator(IMAGE_FILE_SIZE_IN_BYTES)])