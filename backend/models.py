from django.db import models

# Create your models here.
class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=12, decimal_places=10)
    photo = models.ImageField()
    date = models.DateField()

    def __str__(self):
        return self.name

class Lesson(models.Model):
    pin_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, primary_key=True)
    max_grade = models.IntegerField()
    name_lesson = models.CharField(max_length=100)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.name_lesson