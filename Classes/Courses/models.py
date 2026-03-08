from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    hours = models.IntegerField()
    students = models.ManyToManyField('Students.Student', related_name='courses', blank=True)

    def __str__(self):
        return self.name