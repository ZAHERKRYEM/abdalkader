from rest_framework import serializers
<<<<<<< HEAD
from .models import Student, StudentResult, Teacher, Subject,CustomUser

import random, string
=======
from .models import Student, StudentResult, Teacher, Subject

>>>>>>> 16330f09d40fdf7114f9bdfafeddda4cc1a8565e


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
<<<<<<< HEAD
        fields = "__all__"





class UserCreateSerializer(serializers.ModelSerializer):
    generated_password = serializers.CharField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ["id_number","user_type", "generated_password"]

    def create(self, validated_data):
        # توليد كلمة مرور عشوائية
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        user = CustomUser.objects.create_user(
            id_number=validated_data.pop("id_number"),
            password=password,
            **validated_data
        )
        user.generated_password = password
        return user
=======
        fields = "__all__"
>>>>>>> 16330f09d40fdf7114f9bdfafeddda4cc1a8565e
