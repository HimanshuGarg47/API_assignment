from django.urls import path, include
# from rest_framework import routers
from .views import WorkViewSet, RegistrationAPIView, ArtistViewSet

urlpatterns = [
    path('api/register/', RegistrationAPIView.as_view(), name='register'),
]
