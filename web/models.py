from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, id_number, password=None, **extra_fields):
        if not id_number:
            raise ValueError("يجب إدخال رقم التعريف")
        user = self.model(id_number=id_number, **extra_fields)
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_superuser(self, id_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(id_number, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    USER_TYPES = (
        ("student", "Student"),
        ("teacher", "Teacher"),
        ("admin", "Admin"),
    )

    id_number = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPES)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "id_number"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.id_number} - {self.user_type}"




class Student(models.Model):
    id_number = models.CharField(max_length=20,unique=True)  # الرقم التسلسلي
=======


class Student(models.Model):
    serial_number = models.AutoField(primary_key=True)  # الرقم التسلسلي
>>>>>>> 16330f09d40fdf7114f9bdfafeddda4cc1a8565e
    old_registration_number = models.CharField(max_length=50, blank=True, null=True)  # رقم القيد السابق
    
    first_name = models.CharField(max_length=100)   # اسم الطالب
    last_name = models.CharField(max_length=100)    # اللقب
    father_name = models.CharField(max_length=100, blank=True, null=True)  # اسم الأب
    father_job = models.CharField(max_length=150, blank=True, null=True)   # مهنة الأب
    grandfather_name = models.CharField(max_length=100, blank=True, null=True)  # اسم الجد
    mother_name = models.CharField(max_length=100, blank=True, null=True)  # اسم الأم

    birth_place = models.CharField(max_length=150, blank=True, null=True)  # مكان الولادة
    birth_date = models.DateField(blank=True, null=True)                   # تاريخ الولادة
    registration_place_number = models.CharField(max_length=100, blank=True, null=True)  # محل ورقم القيد
    nationality = models.CharField(max_length=100, blank=True, null=True)  # الجنسية

    school_join_date = models.DateField(blank=True, null=True)  # تاريخ الانتساب للمدرسة
    previous_high_school = models.CharField(max_length=200, blank=True, null=True)  # الثانوية التي انتقل منها
    admission_doc_number = models.CharField(max_length=50, blank=True, null=True)  # رقم وثيقة الانتساب
    admission_doc_date = models.DateField(blank=True, null=True)  # تاريخ وثيقة الانتساب
    joined_grade = models.CharField(max_length=50, blank=True, null=True)  # الصف الذي انتسب اليه
    failed_grades_before_joining = models.TextField(blank=True, null=True)  # الصفوف التي رسب فيها قبل انتسابه للمدرسة

    # معلومات حول الخروج (إذا كان موجود)
    leaving_date = models.DateField(blank=True, null=True)
    leaving_reason = models.TextField(blank=True, null=True)
    next_high_school = models.CharField(max_length=200, blank=True, null=True)  # الثانوية التي انتقل اليها
    leaving_doc_type = models.CharField(max_length=100, blank=True, null=True)
    leaving_doc_number = models.CharField(max_length=50, blank=True, null=True)
    leaving_doc_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class StudentResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="results")
    academic_year = models.CharField(max_length=20)  # مثال: 2022/2023
    result = models.TextField()  # ممكن نخليها JSON لو النتائج مفصلة بالمواد
    
    def __str__(self):
        return f"{self.student} - {self.academic_year}"



class Teacher(models.Model):
<<<<<<< HEAD
    id_number = models.CharField(max_length=20,unique=True)
=======
    serial_number = models.AutoField(primary_key=True)
>>>>>>> 16330f09d40fdf7114f9bdfafeddda4cc1a8565e
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100, blank=True, null=True)
    mother_name = models.CharField(max_length=100, blank=True, null=True)

    birth_date = models.DateField(blank=True, null=True)
    birth_place = models.CharField(max_length=150, blank=True, null=True)
    nationality = models.CharField(max_length=100, blank=True, null=True)

    hire_date = models.DateField(blank=True, null=True)
    job_title = models.CharField(max_length=150, blank=True, null=True)
    qualification = models.CharField(max_length=200, blank=True, null=True)
    specialization = models.CharField(max_length=150, blank=True, null=True)

    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Subject(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=50, unique=True)
    teachers = models.ManyToManyField(Teacher, related_name="subjects", blank=True)

    def __str__(self):
        return self.name