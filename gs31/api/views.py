from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from.models import Student

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filterset_fields = ['city']
    filterset_fields = [ 'name','city']
    
    
