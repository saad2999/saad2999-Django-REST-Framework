from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['POST', 'GET'])
def hello_world(request):
    if request.method == 'GET':
        return Response({"message": "This is GET request"})
    if request.method == 'POST':
        print(request.data)
        return Response({"message": "This is POST request", "data": request.data})