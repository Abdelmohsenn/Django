from django.shortcuts import render, get_object_or_404
from .models import Course


def course_list(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'Courses/course_list.html', context)


def course_students(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    students = course.students.all()
    context = {
        'course': course,
        'students': students
    }
    return render(request, 'Courses/course_students.html', context)
