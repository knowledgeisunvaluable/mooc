from django_filters import rest_framework as filters

from course.models import Course, CourseResource, Lesson

class CourseFilter(filters.FilterSet):
    class Meta:
        model = Course
        fields = "__all__"

class CourseResourceFilter(filters.FilterSet):
    class Meta:
        model = CourseResource
        fields = "__all__"

class LessonFilter(filters.FilterSet):
    class Meta:
        model = Lesson
        fields = "__all__"