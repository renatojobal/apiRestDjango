# Django imports
# ..

# Rest_framework imports
from rest_framework import serializers


# Local imports
from core.models import (Student)




class StudentSerializer(serializers.ModelSerializer):
    """
    Seriualizer of the model Student
    """
    class Meta:
        model = Student
        fields = "__all__"