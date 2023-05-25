from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers
from .api.viewsets import PdiViewSet
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'pdi', PdiViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('pdi/', include('rest_framework.urls', namespace='rest_framework1')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
