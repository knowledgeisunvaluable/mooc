import datetime
import time

from rest_framework import serializers
from course.models import Course, CourseResource, Lesson, CourseTag, CourseStudent

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class CourseResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseResource
        fields = "__all__"

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"

class CourseTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseTag
        fields = "__all__"

class CourseStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseStudent
        fields = "__all__"

