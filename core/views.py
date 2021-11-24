from django.shortcuts import render

from core.models import (Student)
from rest_framework import viewsets
from core.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


class StudentViewSet(viewsets.ModelViewSet):
    """
    View set for viewing and editing student instances.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        return self.request.user.accounts.all()


@api_view(['GET'])
def list_students(request):
    """
    View function for listing all students.
    """
    queryset = Student.objects.all()
    serializer = Student(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['GET'])
def get_student(request, pk):
    """
    View function for getting a student.
    """
    student = Student.objects.get(pk=pk)
    return render(request, 'get_student.html', {'student': student})


@api_view(['GET'])
def get_student_by_filter(request, filter_name, filter_value):
    """
    View function for getting a student by filter.
    """
    student = Student.objects.get(**{filter_name: filter_value})
    return render(request, 'get_student.html', {'student': student})

@api_view(['POST'])
def create_student(request):
    """
    View function for creating a student.
    """
    student = Student.objects.create(**request.data)
    return render(request, 'get_student.html', {'student': student})

@api_view(['PUT'])
def update_student(request, pk):
    """
    View function for updating a student.
    """
    student = Student.objects.get(pk=pk)
    student.name = request.data['name']
    student.save()
    return render(request, 'get_student.html', {'student': student})

@api_view(['DELETE'])
def delete_student(request, pk):
    """
    View function for deleting a student.
    """
    student = Student.objects.get(pk=pk)
    student.delete()
    return Response(status=204)

    



