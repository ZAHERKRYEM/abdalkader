from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from web.models import CustomUser
from web.models import Student, Teacher
from rest_framework import permissions, status

from web.models import Student, Teacher
from web.serializers import StudentSerializer, TeacherSerializer



class LoginView(APIView):
    """
    تسجيل الدخول للطالب أو المدرس
    """
    def post(self, request):
        id_number = request.data.get("id_number")
        password = request.data.get("password")

        user = authenticate(request, id_number=id_number, password=password)
        if not user:
            return Response({"error": "رقم التعريف أو كلمة المرور غير صحيحة"}, status=400)

        token, _ = Token.objects.get_or_create(user=user)

        data = {
            "token": token.key,
            "user_type": user.user_type,
            "id_number": user.id_number,
            "first_name": user.first_name,
            "last_name": user.last_name,
        }

        # بيانات الطالب
        if user.user_type == "student":
            try:
                student = Student.objects.get(id_number=user.id_number)
                data["student_data"] = StudentSerializer(student).data
            except Student.DoesNotExist:
                data["student_data"] = None

        # بيانات المدرس
        elif user.user_type == "teacher":
            try:
                teacher = Teacher.objects.get(id_number=user.id_number)
                data["teacher_data"] = TeacherSerializer(teacher).data
            except Teacher.DoesNotExist:
                data["teacher_data"] = None

        return Response(data)





class ProfileView(APIView):
    """
    جلب معلومات الملف الشخصي للطالب أو المدرس حسب المستخدم المسجل دخول
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user

        data = {
            "id_number": user.id_number,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "user_type": user.user_type,
        }

        # بيانات الطالب
        if user.user_type == "student":
            try:
                student = Student.objects.get(id_number=user.id_number)
                data["profile"] = StudentSerializer(student).data
            except Student.DoesNotExist:
                data["profile"] = None

        # بيانات المدرس
        elif user.user_type == "teacher":
            try:
                teacher = Teacher.objects.get(id_number=user.id_number)
                data["profile"] = TeacherSerializer(teacher).data
            except Teacher.DoesNotExist:
                data["profile"] = None

        else:
            data["profile"] = "لا يوجد ملف شخصي لهذا النوع من المستخدمين."

        return Response(data, status=status.HTTP_200_OK)
