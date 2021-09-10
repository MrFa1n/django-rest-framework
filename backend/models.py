from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    salary = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='teachers', blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    pin_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    max_grade = models.IntegerField(blank=True, null=True)
    name_lesson = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.name_lesson