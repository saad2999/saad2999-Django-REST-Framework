from django.contrib import admin
from api import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import ( 
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenVerifyView,
) 

router = DefaultRouter()

router.register('studentapi', views.StudentViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'),
    
    
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
