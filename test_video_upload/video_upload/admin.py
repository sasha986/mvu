from django.contrib import admin

from .forms import UploadVideoModelForm
from .models import Video

# Video upload admin model
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    form = UploadVideoModelForm
    list_display = ['id', 'title', 'video', 'thumbnail', 'user']
    
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)