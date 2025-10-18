from django.contrib import admin
from .models import CustomUser,Student,StudentResult,Subject,Teacher
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Student)
admin.site.register(StudentResult)
admin.site.register(Subject)
admin.site.register(Teacher)