from django.db import models

# Create your models here.


class Student(models.Model):
    """
    Modelo de Book_In_General
    Atributos:
        id
        name
        lastname
        age
    """
    # * Llave primaria
    # Provided by django

    # * Atributos propios
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name

