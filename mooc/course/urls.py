"""course URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path, include, path
from rest_framework.routers import DefaultRouter

from course.views import GetAllCourseAPI, GetCourseAPI, GetCourseByNameAPI, GetCourseresourceByNameAPI, \
    GetLessonByNameAPI, GetCourseByTagAPI, GetCourseByCategoryAPI, UpdateCourseAPI, \
    DeleteCourseAPI, GetAllCourseresourceAPI, GetAllLessonAPI, HelloworldAPI, GetCourseresourceAPI, PostCourseresourceAPI, \
    UpdateCourseresourceAPI, DeleteCourseresourceAPI, GetLessonAPI, PostLessonAPI, UpdateLessonAPI, DeleteLessonAPI, \
    ResourceDownloadAPI, GetTagByCourseAPI, PostCourseAPI, UpdateCoursetagAPI, PostCoursestudentAPI, DeleteCoursestudentAPI, GetStudentByCourseAPI

urlpatterns = [
    re_path(r'^hello/', HelloworldAPI.as_view()),
    re_path(r"^get-all-course/", GetAllCourseAPI.as_view()),
    re_path(r"^get-course/?$", GetCourseAPI.as_view()),
    re_path(r"^get-course-by-name/?$", GetCourseByNameAPI.as_view()),
    re_path(r"^get-courseresource-by-name/?$", GetCourseresourceByNameAPI.as_view()),
    re_path(r"^get-lesson-by-name/?$", GetLessonByNameAPI.as_view()),
    re_path(r"^get-course-by-tag/?$", GetCourseByTagAPI.as_view()),
    re_path(r"^get-course-by-category/?$", GetCourseByCategoryAPI.as_view()),
    re_path(r"^get-all-courseresource/?$", GetAllCourseresourceAPI.as_view()),
    re_path(r"^get-all-lesson/?$", GetAllLessonAPI.as_view()),
    re_path(r"^get-courseresource/?$", GetCourseresourceAPI.as_view()),
    re_path(r"^get-lesson/?$", GetLessonAPI.as_view()),
    re_path(r"^get-tag-by-course", GetTagByCourseAPI.as_view()),
    re_path(r"^get-student-by-course/?$", GetStudentByCourseAPI.as_view()),

    re_path(r"^post-courseresource", PostCourseresourceAPI.as_view()),
    re_path(r"^post-coursestudent", PostCoursestudentAPI.as_view()),
    re_path(r"^post-course", PostCourseAPI.as_view()),
    re_path(r"^post-lesson", PostLessonAPI.as_view()),

    re_path(r"^update-courseresource", UpdateCourseresourceAPI.as_view()),
    re_path(r"^update-coursetag", UpdateCoursetagAPI.as_view()),
    re_path(r"^update-course", UpdateCourseAPI.as_view()),
    re_path(r"^update-lesson", UpdateLessonAPI.as_view()),

    re_path(r"^delete-courseresource/?$", DeleteCourseresourceAPI.as_view()),
    re_path(r"^delete-coursestudent/?$", DeleteCoursestudentAPI.as_view()),
    re_path(r"^delete-course/?$", DeleteCourseAPI.as_view()),
    re_path(r"^delete-lesson/?$", DeleteLessonAPI.as_view()),

    re_path(r"^resource-download", ResourceDownloadAPI.as_view()),
]