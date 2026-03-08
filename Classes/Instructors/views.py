from django.shortcuts import render, get_object_or_404
from .models import Instructor


def instructor_list(request):
    instructors = Instructor.objects.all()
    context = {
        'instructors': instructors
    }
    return render(request, 'Instructors/instructor_list.html', context)


def instructor_courses(request, instructor_id):
    instructor = get_object_or_404(Instructor, pk=instructor_id)
    courses = instructor.courses.all()
    context = {
        'instructor': instructor,
        'courses': courses
    }
    return render(request, 'Instructors/instructor_courses.html', context)
