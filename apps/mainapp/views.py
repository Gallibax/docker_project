from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Student, Course
from .serializers import StudentSerializer, CourseSerializer, ListCourseSerializer, DetailCourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return ListCourseSerializer
        elif self.action == 'retrieve':
            return DetailCourseSerializer
        return CourseSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


