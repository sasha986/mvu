from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient

from django.contrib.auth.models import User
from .models import Video

class UploadVideoTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='admin', email='admin@test.local', password='admin')
        # Login user
        self.client.force_authenticate(self.user)
    
    # Successful upload of supported video format and supported thumbnail image format
    def test_upload_video_successful(self):    
        # create a test video file and thumbnail
        with open("../test/test.mp4", "rb") as vf:
            video_file = SimpleUploadedFile('test_video.mp4', vf.read(), content_type='video/mp4')
        with open("../test/test.jpg", "rb") as im:
            thumbnail_file = SimpleUploadedFile('test_thumb.jpg', im.read(), content_type='image/jpg')
        
        # Upload the video file
        response = self.client.post(reverse('video_upload:video_upload'), {
            'title': 'Test Video!',
            'description': 'This is just a test video!',
            'thumbnail': thumbnail_file,
            'video': video_file,
        }, format='multipart')
        
        # Check that the video was uploaded successfully
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Video.objects.count(), 1)
        
        video = Video.objects.first()
        self.assertEqual(video.title, 'Test Video!')
        self.assertEqual(video.description, 'This is just a test video!')
        self.assertEqual(video.user, self.user)
    
    
    # Failed to upload not supported video format and not supported thumbnail image format    
    def test_upload_video_failed(self):
        # create a test video file and thumbnail
        with open("../test/test.ogg", "rb") as vf:
            video_file = SimpleUploadedFile('test_video.ogg', vf.read(), content_type='video/ogg')
        with open("../test/test.webp", "rb") as im:
            thumbnail_file = SimpleUploadedFile('test_thumb.webp', im.read(), content_type='image/webp')
        
        # Upload the video file
        response = self.client.post(reverse('video_upload:video_upload'), {
            'title': 'Test Video!',
            'description': 'This is just a test video!',
            'thumbnail': thumbnail_file,
            'video': video_file,
        }, format='multipart')
        
        # Check that the video was uploaded successfully
        self.assertEqual(response.status_code, 400)
        self.assertIn('is not an acceptable file type', response.data['video'][0])
        self.assertIn('is not an acceptable file type', response.data['thumbnail'][0])
        self.assertEqual(Video.objects.count(), 0)
               
        