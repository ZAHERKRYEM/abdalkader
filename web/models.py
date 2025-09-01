from django.db import models


class Student(models.Model):
    serial_number = models.AutoField(primary_key=True)  # الرقم التسلسلي
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
