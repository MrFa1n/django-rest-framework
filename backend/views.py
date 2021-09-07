from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from .serializers import TeacherSerializer, LessonSerializer
from .models import Teacher, Lesson

# Create your views here.
class ListTeacherAPIView(ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class CreateTeacherAPIView(CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class UpdateTeacherAPIView(UpdateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class DeleteTeacherAPIView(DestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class ListLessonAPIView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class CreateLessonAPIView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class UpdateLessonAPIView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class DeleteLessonAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer