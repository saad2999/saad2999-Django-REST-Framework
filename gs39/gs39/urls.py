from django.contrib import admin
from api import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('singer', views.SingerViewSet, basename='Singer')
router.register('song', views.SongViewSet, basename='Song')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
