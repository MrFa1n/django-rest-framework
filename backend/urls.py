from django.urls import path
from backend import views

urlpatterns = [
    path("teacher/", views.ListTeacherAPIView.as_view(), name="list_teacher"),
    path("teacher/create/", views.CreateTeacherAPIView.as_view(), name="create_teacher"),
    path("teacher/update/<int:pk>/", views.UpdateTeacherAPIView.as_view(), name="update_teacher"),
    path("teacher/delete/<int:pk>/", views.DeleteTeacherAPIView.as_view(), name="delete_teacher"),
    
    path("lesson/", views.ListLessonAPIView.as_view(), name="list_lesson"),
    path("lesson/create/", views.CreateLessonAPIView.as_view(), name="create_lesson"),
    path("lesson/update/<int:pk>/", views.UpdateLessonAPIView.as_view(), name="update_lesson"),
    path("lesson/delete/<int:pk>/", views.DeleteLessonAPIView.as_view(), name="delete_lesson"),
]