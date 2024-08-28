from django.shortcuts import render
from django.http import HttpResponse
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        print(json_data)
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        seriaize_data=StudentSerializer(data=python_data)
        if seriaize_data.is_valid():
            seriaize_data.save()
            res={"msg":"Data created"}
            json_data=JSONRenderer().render(res)
    
            return HttpResponse(json_data, content_type='application/json')
        else:
             json_data=JSONRenderer().render(seriaize_data.errors)
             return HttpResponse(json_data, content_type='application/json')

