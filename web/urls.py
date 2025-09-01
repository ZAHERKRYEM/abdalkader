from django.urls import path
from .views import (
    StudentListCreateAPIView, StudentRetrieveUpdateDestroyAPIView,
    StudentResultListCreateAPIView, StudentResultRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    # Students
    path("api/students/", StudentListCreateAPIView.as_view(), name="student-list-create"),
    path("api/students/<int:pk>/", StudentRetrieveUpdateDestroyAPIView.as_view(), name="student-detail"),
    
    # Student Results
    path("api/results/", StudentResultListCreateAPIView.as_view(), name="result-list-create"),
    path("api/results/<int:pk>/", StudentResultRetrieveUpdateDestroyAPIView.as_view(), name="result-detail"),
]
