from django.urls import path
from . import views

urlpatterns = [
    path('', views.instructor_list, name='instructor_list'),
    path('<int:instructor_id>/', views.instructor_courses, name='instructor_courses'),
]
