from rest_framework import serializers
from .validators import MimetypeValidator, FileSizeValidator

from .models import Video

# file types and file size limiations  
VIDEO_CONTENT_TYPES = ('video/mp4',) # allowed video file types
IMAGE_CONTENT_TYPES = ('image/png', 'image/jpeg', 'image/jpg',) # allowed images file types
VIDEO_FILE_SIZE_IN_BYTES = 1024 * 1024 * 10  # max allowed video file size ~10 Mib
IMAGE_FILE_SIZE_IN_BYTES = 1024 * 1024 # max allowed thumbnail file size ~1 Mb


class VideoSerializer(serializers.ModelSerializer):
    """
    Validates file type (mimetype)
    """
    
    video = serializers.FileField(validators=[MimetypeValidator(VIDEO_CONTENT_TYPES), FileSizeValidator(VIDEO_FILE_SIZE_IN_BYTES)])
    thumbnail = serializers.ImageField(validators=[MimetypeValidator(IMAGE_CONTENT_TYPES), FileSizeValidator(IMAGE_FILE_SIZE_IN_BYTES)])
    
    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'video', 'thumbnail', 'uploaded_dt']
        read_only_fields = ['id', 'uploaded_dt']
        
    def create(self, validated_data):
        """
        Create and return a new `Video` instance, given the validated data.
        """
        return Video.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `Video` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.description = validate_data.get('title', instance.description)
        instance.thumbnail = validated_data.get('thumbnail', instance.thumbnail)
        instance.video = validated_data.get('video', instance.video)
        instance.save()
        
        return instance
    