from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views

app_name = 'login'

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token)
]