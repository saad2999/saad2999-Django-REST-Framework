from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer

def student_detail(request,pk):
    stu=Student.objects.get(id=pk)
    serializer=StudentSerializer(stu)
    
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')


def student_all(request):
    stu=Student.objects.all()
    serializer=StudentSerializer(stu,many=True)
    
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

    

