from django.urls import path
from rest_framework.documentation import include_docs_urls

from .views import (
    VideoListAPIView,
    VideoAPIView
)

app_name = 'video_upload'

urlpatterns = [
    path('video/list/', VideoListAPIView.as_view(), name='my_videos'),
    path('video/<id>/', VideoAPIView.as_view(), name='video_details'),
    path('video/upload/', VideoAPIView.as_view(), name='video_upload'),
    path('docs/', include_docs_urls(title='Video Upload API')),
]