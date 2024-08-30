from django_filters import FilterSet, filters, CharFilter, NumberFilter
from .models import School, Classroom, Teacher, Student

# code here
class SchoolFilter(FilterSet):
    # Filtering by name with partial matching (case-insensitive)
    name = CharFilter(field_name='name', lookup_expr='icontains')  

    class Meta:
        model = School
        fields = ['name']


class ClassroomFilter(FilterSet):
    # Filtering by school using the school ID
    school = NumberFilter(field_name='school__id')  

    class Meta:
        model = Classroom
        fields = ['school']


class TeacherFilter(FilterSet):
    # Filtering by first and last name with partial matching
    first_name = CharFilter(field_name='first_name', lookup_expr='icontains')
    last_name = CharFilter(field_name='last_name', lookup_expr='icontains')
    # Filtering by gender with exact matching
    gender = CharFilter(field_name='gender', lookup_expr='exact')
    # Filtering by school ID through classroom relationships
    school = NumberFilter(field_name='classrooms__school__id', lookup_expr='exact')  
    # Filtering by classroom ID
    classroom = NumberFilter(field_name='classrooms__id', lookup_expr='exact')

    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'gender', 'classroom', 'school']


class StudentFilter(FilterSet):
    # Filtering by first and last name with partial matching
    first_name = CharFilter(field_name='first_name', lookup_expr='icontains')
    last_name = CharFilter(field_name='last_name', lookup_expr='icontains')
    # Filtering by gender with exact matching
    gender = CharFilter(field_name='gender', lookup_expr='exact')
    # Filtering by school ID through classroom relationship
    school = NumberFilter(field_name='classroom__school__id', lookup_expr='exact')  
    # Filtering by classroom ID
    classroom = NumberFilter(field_name='classroom__id', lookup_expr='exact')  

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'gender', 'classroom', 'school']