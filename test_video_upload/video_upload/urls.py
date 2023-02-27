from django.urls import path

from .views import (
    VideoListAPIView,
    VideoAPIView,
    VideoUploadAPIView
)

app_name = 'video_upload'

# urls for upload, update and delete video and video list
urlpatterns = [
    path('video/list', VideoListAPIView.as_view(), name='my_videos'),
    path('video/<id>', VideoAPIView.as_view(), name='video_details'),
    path('video/upload', VideoUploadAPIView.as_view(), name='video_upload'),
]