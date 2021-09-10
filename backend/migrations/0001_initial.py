# Generated by Django 3.2.2 on 2021-09-09 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('salary', models.FloatField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='teachers')),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_grade', models.IntegerField(blank=True, null=True)),
                ('name_lesson', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('pin_teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.teacher')),
            ],
        ),
    ]
