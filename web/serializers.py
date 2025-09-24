from rest_framework import serializers
from .models import Student, StudentResult, Teacher, Subject



class StudentResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentResult
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    results = StudentResultSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = "__all__"


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ["id", "name", "code", "teachers"]
        extra_kwargs = {"teachers": {"required": False}}


class TeacherSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True, read_only=True)

    class Meta:
        model = Teacher
        fields = "__all__"