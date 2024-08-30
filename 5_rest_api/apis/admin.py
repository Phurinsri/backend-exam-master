from django.contrib import admin

# Register your models here.
from .models import School, Classroom, Teacher, Student

admin.site.register(School)
admin.site.register(Classroom)
admin.site.register(Teacher)
admin.site.register(Student)