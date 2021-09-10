from django import forms
from django.forms import fields
from django.forms.models import ModelForm

from .models import Lesson, Teacher

class PostForm (forms.ModelForm):
    class Meta:
        model = Lesson
        fields = "__all__"