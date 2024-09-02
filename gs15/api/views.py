from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def retrieve(self,request, pk=None):
        print('*****************retrieve*****************')
        print('base_name:',self.basename)
        print('Action:',self.action)
        print('detail:',self.detail)
        print('suffix:',self.suffix)
        print('name:',self.name)
        id=pk
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data, status=status.HTTP_200_OK)
       

    def create(self, request, *args, **kwargs):
        print('*****************create*****************')
        print('base_name:',self.basename)
        print('Action:',self.action)
        print('detail:',self.detail)
        print('suffix:',self.suffix)
        print('name:',self.name)
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def update(self, request, pk=None):
            print('*****************update*****************')
            print('base_name:',self.basename)
            print('Action:',self.action)
            print('detail:',self.detail)
            print('suffix:',self.suffix)
            print('name:',self.name)
            id=pk
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu, data=request.data, partial=False)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Data Updated'}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400)
        
    def partial_update (self, request, pk=None):
            print('*****************partial_update*****************')
            print('base_name:',self.basename)
            print('Action:',self.action)
            print('detail:',self.detail)
            print('suffix:',self.suffix)
            print('name:',self.name)
            id=pk
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Data Updated'}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400)
        
    def destroy(self,request, pk=None):
        print('*****************destroy*****************')
        print('base_name:',self.basename)
        print('Action:',self.action)
        print('detail:',self.detail)
        print('suffix:',self.suffix)
        print('name:',self.name)
        stu= Student.objects.get(id=pk)
        stu.delete()
        
        return Response({'msg':'data deleted'},status=status.HTTP_204_NO_CONTENT)
    
    def list(self,request):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)
