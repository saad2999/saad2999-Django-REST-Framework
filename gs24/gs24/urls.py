from django.contrib import admin
from api import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.auth import CustomAuthToken

router = DefaultRouter()

router.register('studentapi', views.StudentViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('gettoken/', CustomAuthToken.as_view(), name='gettoken'),
]
