from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def student_get(request):
    #read
    
    if request.method == 'GET':
        json_data = request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id', None)
        print(id)
        if id is not None:
            student=Student.objects.get(id=id)
            serializer=StudentSerializer(student)
            json_data=JSONRenderer().render(serializer.data)
            print(json_data)
            return HttpResponse(json_data, content_type='application/json')
        students=Student.objects.all()
        serializer=StudentSerializer(students, many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
    #creat
    if request.method == 'POST':
        json_data = request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serializer=StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Created'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    #update
    if request.method == 'PUT':
        json_data = request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id')
        student=Student.objects.get(id=id)
        serializer=StudentSerializer(student, data=python_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Updated'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    #delete
    if request.method == 'DELETE':
        json_data = request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id')
        student=Student.objects.get(id=id)
        student.delete()
        res={'msg':'Data Deleted'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')
            
        
