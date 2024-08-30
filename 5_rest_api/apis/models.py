from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=100, unique=True)
    short_name = models.CharField(max_length=10)
    address = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name

class Classroom(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='classrooms')
    grade  = models.CharField(max_length=10)
    section  = models.CharField(max_length=10)
    
    def __str__(self):
       return f"{self.grade} {self.section} ({self.school.short_name})"
    
class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    classrooms = models.ManyToManyField(Classroom, related_name='teachers')
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='teachers')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='students')
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

