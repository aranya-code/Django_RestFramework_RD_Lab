from django.shortcuts import render
from fvbApp.models import Student
from fvbApp.serializers import StudentSerializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def student_list(request):

    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializers(students,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def student_detail(request,pk):
    try:
        students = Student.objects.get(pk=pk)
    except:
        return Response(status= status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer = StudentSerializers(students)
        return Response(serializer.data)
    
    elif request.method=='PUT':
        serializer = StudentSerializers(students,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        students.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)