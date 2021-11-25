from django.shortcuts import render

from core.models import (Student)
from rest_framework import viewsets
from core.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

class StudentViewSet(viewsets.ModelViewSet):
    """
    View set for viewing and editing student instances.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



@api_view(['GET'])
def list_students(request):
    """
    View function for listing all students.
    """
    if request.method == 'GET':
        queryset = Student.objects.all()
        print(queryset)
        serializer = StudentSerializer(queryset, many=True)

        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['GET', 'PUT', 'DELETE'])
def manage_student(request, id):
    """
    View function for getting a student.
    """


    if request.method == 'GET':
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        student = Student.objects.get(id=id)
        print(student)
        student.name = request.data['name']
        student.lastname = request.data['lastname']
        student.age = request.data['age']
        student.save()
        print(student)
        return Response({'status': 'updated'}, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        Student.objects.get(id=id).delete()
        return Response({'status': 'deleted'}, status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def get_student_by_filter(request):
    """
    View function for getting a student by filter.
    """
    if request.method == 'GET':
        student = Student.objects.get(**{request.data.get("filter"): request.data.get("value")})
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

@api_view(['GET'])
def get_student_by_filter_query_paramans(request):
    """
    View function for getting a student by filter.
    """
    if request.method == 'GET':
        student = Student.objects.get(**{request.query_params.get("filter"): request.query_params.get("value")})
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_student(request):
    """
    View function for creating a student.
    """
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
