from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from models import School, Classroom, Teacher, Student
from serializers import SchoolSerializer, ClassroomSerializer, TeacherSerializer, StudentSerializer
from filters import SchoolFilter, ClassroomFilter, TeacherFilter, StudentFilter

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = StudentFilter