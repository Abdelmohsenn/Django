from django.db import models
from Students.models import Student
from Courses.models import Course
# Create your models here.

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    courses = models.ManyToManyField(Course, related_name='instructors', blank=True)
    
    def __str__(self):
        return self.name