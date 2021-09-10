from rest_framework import serializers
from .models import Teacher, Lesson

class TeacherSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Teacher
		fields = ('name', 'salary', 'photo', 'date')

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('pin_teacher', 'max_grade', 'name_lesson', 'description')