from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView


class StudentAPI(APIView):
    def get(self, request, pk=None):
        id=pk
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data, status=status.HTTP_200_OK)
        stu=Student.objects.all()
        serializer=StudentSerializer(stu, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk):
        id=pk
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        id=pk
        stu=Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'Data Deleted'}, status=status.HTTP_200_OK)
    def patch(self, request, pk):
        id=pk
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=400)
    


