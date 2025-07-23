from rest_framework import serializers
from .models import Student, Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class ListCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'price']

class GetStudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'email']    


class DetailCourseSerializer(serializers.ModelSerializer):
    students_count = serializers.SerializerMethodField()
    students = GetStudentsSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'start_date', 'duration_weeks', 'price', 'students_count', 'students']

    def get_students_count(self, obj):
        return obj.students.count()



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


