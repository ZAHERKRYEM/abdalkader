from django.urls import path
from .views import (
    StudentListCreateAPIView, StudentRetrieveUpdateDestroyAPIView,
    StudentResultListCreateAPIView, StudentResultRetrieveUpdateDestroyAPIView,
    TeacherListCreateAPIView,
    TeacherDetailAPIView,
    SubjectListCreateAPIView,
    SubjectDetailAPIView,
    RegisterView
)


urlpatterns = [

    path("api/register/",RegisterView.as_view()),
    # Students
    path("api/students/", StudentListCreateAPIView.as_view(), name="student-list-create"),
    path("api/students/<int:pk>/", StudentRetrieveUpdateDestroyAPIView.as_view(), name="student-detail"),
    
    # Student Results
    path("api/results/", StudentResultListCreateAPIView.as_view(), name="result-list-create"),
    path("api/results/<int:pk>/", StudentResultRetrieveUpdateDestroyAPIView.as_view(), name="result-detail"),
    
    # Teacher URLs
    path("api/teachers/", TeacherListCreateAPIView.as_view(), name="teacher-list-create"),
    path("api/teachers/<int:pk>/", TeacherDetailAPIView.as_view(), name="teacher-detail"),

    # Subject URLs
    path("api/subjects/", SubjectListCreateAPIView.as_view(), name="subject-list-create"),
    path("api/subjects/<int:pk>/", SubjectDetailAPIView.as_view(), name="subject-detail"),
]
