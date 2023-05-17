from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers
from .api.viewsets import MeetingViewSet

router = routers.DefaultRouter()
router.register(r'meeting', MeetingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('meeting/', include('rest_framework.urls', namespace='rest_framework')),
]
