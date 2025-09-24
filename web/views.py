from rest_framework import generics
from .models import Student, StudentResult,Teacher, Subject
from .serializers import StudentSerializer, StudentResultSerializer,TeacherSerializer, SubjectSerializer
from django.db.models import Q


# ================== Students ==================
class StudentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        queryset = Student.objects.all()
        params = self.request.query_params

        # البحث في كل الحقول
        if 'serial_number' in params:
            queryset = queryset.filter(serial_number=params['serial_number'])
        if 'old_registration_number' in params:
            queryset = queryset.filter(old_registration_number__icontains=params['old_registration_number'])
        if 'first_name' in params:
            queryset = queryset.filter(first_name__icontains=params['first_name'])
        if 'last_name' in params:
            queryset = queryset.filter(last_name__icontains=params['last_name'])
        if 'father_name' in params:
            queryset = queryset.filter(father_name__icontains=params['father_name'])
        if 'father_job' in params:
            queryset = queryset.filter(father_job__icontains=params['father_job'])
        if 'grandfather_name' in params:
            queryset = queryset.filter(grandfather_name__icontains=params['grandfather_name'])
        if 'mother_name' in params:
            queryset = queryset.filter(mother_name__icontains=params['mother_name'])
        if 'birth_place' in params:
            queryset = queryset.filter(birth_place__icontains=params['birth_place'])
        if 'birth_date' in params:
            queryset = queryset.filter(birth_date=params['birth_date'])
        if 'registration_place_number' in params:
            queryset = queryset.filter(registration_place_number__icontains=params['registration_place_number'])
        if 'nationality' in params:
            queryset = queryset.filter(nationality__icontains=params['nationality'])
        if 'school_join_date' in params:
            queryset = queryset.filter(school_join_date=params['school_join_date'])
        if 'previous_high_school' in params:
            queryset = queryset.filter(previous_high_school__icontains=params['previous_high_school'])
        if 'admission_doc_number' in params:
            queryset = queryset.filter(admission_doc_number__icontains=params['admission_doc_number'])
        if 'admission_doc_date' in params:
            queryset = queryset.filter(admission_doc_date=params['admission_doc_date'])
        if 'joined_grade' in params:
            queryset = queryset.filter(joined_grade__icontains=params['joined_grade'])
        if 'failed_grades_before_joining' in params:
            queryset = queryset.filter(failed_grades_before_joining__icontains=params['failed_grades_before_joining'])
        if 'leaving_date' in params:
            queryset = queryset.filter(leaving_date=params['leaving_date'])
        if 'leaving_reason' in params:
            queryset = queryset.filter(leaving_reason__icontains=params['leaving_reason'])
        if 'next_high_school' in params:
            queryset = queryset.filter(next_high_school__icontains=params['next_high_school'])
        if 'leaving_doc_type' in params:
            queryset = queryset.filter(leaving_doc_type__icontains=params['leaving_doc_type'])
        if 'leaving_doc_number' in params:
            queryset = queryset.filter(leaving_doc_number__icontains=params['leaving_doc_number'])
        if 'leaving_doc_date' in params:
            queryset = queryset.filter(leaving_doc_date=params['leaving_doc_date'])

        return queryset


class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# ================== Student Results ==================
class StudentResultListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = StudentResultSerializer

    def get_queryset(self):
        queryset = StudentResult.objects.all()
        params = self.request.query_params

        if 'id' in params:
            queryset = queryset.filter(id=params['id'])
        if 'academic_year' in params:
            queryset = queryset.filter(academic_year__icontains=params['academic_year'])
        if 'result' in params:
            queryset = queryset.filter(result__icontains=params['result'])
        if 'student_first_name' in params:
            queryset = queryset.filter(student__first_name__icontains=params['student_first_name'])
        if 'student_last_name' in params:
            queryset = queryset.filter(student__last_name__icontains=params['student_last_name'])
        if 'student_serial_number' in params:
            queryset = queryset.filter(student__serial_number=params['student_serial_number'])

        return queryset


class StudentResultRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentResult.objects.all()
    serializer_class = StudentResultSerializer





class TeacherListCreateAPIView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        params = self.request.query_params

        filters = Q()
        if "first_name" in params:
            filters &= Q(first_name__icontains=params["first_name"])
        if "last_name" in params:
            filters &= Q(last_name__icontains=params["last_name"])
        if "specialization" in params:
            filters &= Q(specialization__icontains=params["specialization"])
        if "job_title" in params:
            filters &= Q(job_title__icontains=params["job_title"])
        if "email" in params:
            filters &= Q(email__icontains=params["email"])
        if "phone_number" in params:
            filters &= Q(phone_number__icontains=params["phone_number"])

        return queryset.filter(filters)


class TeacherDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class SubjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        params = self.request.query_params
        if "name" in params:
            queryset = queryset.filter(name__icontains=params["name"])
        if "code" in params:
            queryset = queryset.filter(code__icontains=params["code"])
        return queryset


class SubjectDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
