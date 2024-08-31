import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class StudentView(View):
    def get(self, request, *args, **kwargs):
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
    def post(self, request, *args, **kwargs):
        
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
    def put(self, request, *args, **kwargs):
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
    def delete(self, request, *args, **kwargs):
            json_data = request.body
            stream=io.BytesIO(json_data)
            python_data=JSONParser().parse(stream)
            id=python_data.get('id')
            student=Student.objects.get(id=id)
            student.delete()
            res={'msg':'Data Deleted'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        
    
 