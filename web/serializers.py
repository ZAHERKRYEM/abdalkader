from rest_framework import serializers
from .models import Student, StudentResult


class StudentResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentResult
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    results = StudentResultSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = "__all__"
