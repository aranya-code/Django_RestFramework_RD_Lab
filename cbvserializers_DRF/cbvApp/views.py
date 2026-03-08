from django.shortcuts import render
from cbvApp.models import Student
from cbvApp.serializers import StudentSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import generics, mixins

# =====================================================================
# CURRENT APPROACH: GenericAPIView + Mixins
# NOTE: This approach reduces boilerplate. GenericAPIView provides the core 
# configuration (queryset, serializer_class), while the Mixins provide pre-written 
# logic for common tasks so I don't have to manually write save/validation logic.
# =====================================================================

class StudentList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    # These two variables are required by GenericAPIView so the mixins know what to use.
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def get(self, request):
        # self.list() comes from ListModelMixin. It automatically fetches the queryset, 
        # passes it to the serializer with many=True, and returns a formatted Response.
        return self.list(request)
    
    def post(self, request):
        # self.create() comes from CreateModelMixin. It automatically checks serializer.is_valid(), 
        # saves to the database, and returns the standard HTTP 201 Created status.
        return self.create(request)
    
class StudentDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, 
                    mixins.DestroyModelMixin, generics.GenericAPIView):
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def get(self, request, pk):
        # self.retrieve() automatically fetches the specific object by pk. 
        # It also handles throwing a 404 automatically if the student doesn't exist.
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        # self.update() handles the full update cycle (validation and saving).
        return self.update(request, pk)
    
    def delete(self, request, pk):
        # self.destroy() deletes the object and automatically returns an HTTP 204 No Content.
        return self.destroy(request, pk)


"""
# =====================================================================
# PREVIOUS APPROACH: Standard APIView (Kept for reference)
# =====================================================================
# This was my initial approach before upgrading to Mixins. 
# It requires writing out all the manual validation, custom responses, and 
# exception handling (like trying to catch DoesNotExist errors manually). 

class StudentList(APIView):

    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializers(students, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class StudentDetail(APIView):
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializers(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializers(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""