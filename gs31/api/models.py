from django.db import models

from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    roll=models.IntegerField()
    city=models.CharField(max_length=50)
    passby=models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name
    
