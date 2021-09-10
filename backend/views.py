from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView 
from .serializers import TeacherSerializer, LessonSerializer
from .models import Teacher, Lesson
from .forms import PostForm

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

def all_lesson(request):
    lesson = Lesson.objects.all()
    return render(request, "lesson/all_lesson.html", {"lesson": lesson})

def list_and_add_lesson(request):
    context = {}
    context['form']= PostForm()
    form = PostForm(request.POST)
    if form.is_valid():
        form.save()
        all_lesson()
    return render(request, "lesson/index.html", context)