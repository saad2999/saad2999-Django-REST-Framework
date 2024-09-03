from django.contrib import admin
from api import views
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('studentapi/', views.StudentList.as_view()),
]
