from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .serializers import VideoSerializer
from .models import Video


class VideoListAPIView(APIView):
    """
    VideoListAPIView returns a list of all video uploaded by user.
    """
    
    allowed_methods = ['GET']
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(responses={200: VideoSerializer(many=True)})
    def get(self, request):
        
        videos = Video.objects.filter(user=request.user)
        serializer = VideoSerializer(videos, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class VideoAPIView(APIView):
    """
    VideoAPIView returns video by ID and delete video by ID
    """
    
    allowed_methods = ['GET', 'POST', 'PATCH', 'DELETE']
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    # Get video by ID
    @swagger_auto_schema(responses={200: VideoSerializer()})
    def get(self, request, id=None):
        try:
            video = Video.objects.get(user=request.user, id=id)
        except Video.DoesNotExist:
            return Response({'error': 'Video does not exits!'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = VideoSerializer(video)
        return Response(serializer.data)
    
    # Delete uploaded video by ID
    @swagger_auto_schema(responses={204: 'Video deleted successfully!'}, operation_description="description")
    def delete(self, request):
        try:
            video = Video.objects.get(user=request.user, id=id)
        except Video.DoesNotExist:
            return Response({'error': 'Video does not exits!'}, status=status.HTTP_404_NOT_FOUND)
        
        video.delete()
        return Response({'ok': 'Video deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


class VideoUploadAPIView(APIView):
    """
    VideoAPIView upload video, update video by ID
    """
    
    allowed_methods = ['POST', 'PATCH']
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    # Upload video
    @swagger_auto_schema(responses={201: VideoSerializer()})
    def post(self, request, id=None):
        serializer = VideoSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.validated_data['user'] = request.user
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    # Update video details for video ID
    @swagger_auto_schema(responses={200: VideoSerializer()})
    def patch(self, request, id=None):
        try:
            video = Video.objects.get(user=request.user, id=id)
        except Video.DoesNotExist:
            return Response({'error': 'Video does not exits!'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = VideoSerializer(video, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.validated_data['user'] = request.user
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_200_OK)