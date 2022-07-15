from course.serializers import CourseSerializer, CourseResourceSerializer, LessonSerializer, CourseTagSerializer, CourseStudentSerializer
from course.models import Course, CourseResource, Lesson, CourseTag, CourseStudent

from utils.api import APIView

from django.http import StreamingHttpResponse
import logging
import os
import django.utils.timezone as timezone

logger = logging.getLogger('mdjango')

class GetAllCourseAPI(APIView):
    def get(self, request):
        res = Course.objects.all()
        return self.success(self.paginate_data(request, res, CourseSerializer))

class GetCourseAPI(APIView):
    def get(self, request):
        data = request.data
        id = data["id"]
        res = Course.objects.filter(id=id)
        return self.success(self.paginate_data(request, res, CourseSerializer))

class GetAllCourseresourceAPI(APIView):
    def get(self, request):
        data = request.data
        course_id = data["course_id"]
        res = CourseResource.objects.filter(course_id=course_id)
        return self.success(self.paginate_data(request, res, CourseResourceSerializer))

class GetCourseresourceAPI(APIView):
    def get(self, request):
        data = request.data
        id = data["id"]
        res = CourseResource.objects.filter(id=id)
        return self.success(self.paginate_data(request, res, CourseResourceSerializer))

class GetAllLessonAPI(APIView):
    def get(self, request):
        data = request.data
        course_id = data["course_id"]
        res = Lesson.objects.filter(course_id=course_id)
        return self.success(self.paginate_data(request, res, LessonSerializer))

class GetLessonAPI(APIView):
    def get(self, request):
        data = request.data
        id = data["id"]
        res = Lesson.objects.filter(id=id)
        return self.success(self.paginate_data(request, res, LessonSerializer))

class GetCourseByNameAPI(APIView):
    def get(self, request):
        data = request.data
        name = data["name"]
        res = Course.objects.filter(name=name)
        return self.success(self.paginate_data(request, res, CourseSerializer))

class GetCourseresourceByNameAPI(APIView):
    def get(self, request):
        data = request.data
        name = data["name"]
        res = CourseResource.objects.filter(name=name)
        return self.success(self.paginate_data(request, res, CourseResourceSerializer))

class GetLessonByNameAPI(APIView):
    def get(self, request):
        data = request.data
        name = data["name"]
        res = Lesson.objects.filter(name=name)
        return self.success(self.paginate_data(request, res, LessonSerializer))

class GetCourseByCategoryAPI(APIView):
    def get(self, request):
        data = request.data
        category = data["category"]
        res = Course.objects.filter(category=category)
        return self.success(self.paginate_data(request, res, CourseSerializer))

class GetCourseByTagAPI(APIView):
    def get(self, request):
        data = request.data
        course_tag = data["course_tag"]
        courses = CourseTag.objects.filter(course_tag=course_tag).values("course")
        res = Course.objects.filter(id__in=courses)
        return self.success(self.paginate_data(request, res, CourseSerializer))

class GetTagByCourseAPI(APIView):
    def get(self, request):
        data = request.data
        course_id = data["course_id"]
        res = CourseTag.objects.filter(course_id=course_id)
        return self.success(self.paginate_data(request, res, CourseTagSerializer))

class GetStudentByCourseAPI(APIView):
    def get(self, request):
        data = request.data
        course_id = data["course_id"]
        res = CourseStudent.objects.filter(course_id=course_id)
        return self.success(self.paginate_data(request, res, CourseStudentSerializer))

class PostCourseAPI(APIView):
    def post(self, request):
        data = request.data
        name, desc, image, bill, category, teacher_id, detail, learn_times = data["name"], data["desc"], data["image"], data["bill"], data["category"], data["teacher_id"], data["detail"], data["learn_times"]
        if teacher_id == "": return self.error(msg="teacher_id cannot be null")
        if name == "": return self.error(msg="name cannot be null")
        if learn_times == "": learn_times = 0
        res = Course.objects.filter(name=name)
        if len(res) > 0: return self.error(msg="name duplicated")
        res = Course.objects.create(
            name=name,
            desc=desc,
            image=image,
            bill=bill,
            category=category,
            teacher_id=teacher_id,
            detail=detail,
            learn_times=learn_times,
            students_number=0,
            fav_nums=0,
            youneed_know="",
            teacher_tell="",
            add_time=timezone.now(),
        )
        res.save()
        return self.success('create done')

class PostCourseresourceAPI(APIView):
    def post(self, request):
        data = request.data
        name, download, course_id = data["name"], data["download"], data["course_id"]
        if name == "": return self.error(msg="name cannot be null")
        if course_id == "": return self.error(msg="course_id cannot be null")
        if download == "": return self.error(msg="download cannot be null")
        res = CourseResource.objects.filter(name=name)
        if len(res) > 0: return self.error(msg="name duplicated")

        res = CourseResource.objects.create(
            name=name,
            download=download,
            add_time=timezone.now(),
            course_id=course_id
        )
        res.save()
        return self.success('create done')

class PostLessonAPI(APIView):
    def post(self, request):
        data = request.data
        name, course_id, video_id = data["name"], data["course_id"], data["video_id"]
        if name == "": return self.error(msg="name cannot be null")
        if course_id == "": return self.error(msg="course_id cannot be null")
        if video_id == "": return self.error(msg="video_id cannot be null")
        res = Lesson.objects.filter(name=name)
        if len(res) > 0: return self.error(msg="name duplicated")
        res = Lesson.objects.create(
            name=name,
            add_time=timezone.now(),
            course_id=course_id,
            video_id=video_id,
        )
        res.save()
        return self.success('create done')

class PostCoursestudentAPI(APIView):
    def post(self, request):
        data = request.data
        course_id, student_id = data["course_id"], data["student_id"]
        if course_id == "": return self.error(msg="course_id cannot be null")
        if student_id == "": return self.error(msg="student_id cannot be null")
        res = Course.objects.filter(id=course_id)
        if len(res) == 0: return self.error(msg="cannot find course")
        # res = Student.objects.filter(id=student_id)
        # if len(res) == 0: return self.error(msg="cannot find student")

        res = CourseStudent.objects.filter(
            course_id=course_id,
            student_id=student_id
        )
        if len(res) > 0: return self.error(msg="student have joined the course")

        res = CourseStudent.objects.create(
            course_id=course_id,
            student_id=student_id
        )
        res.save()
        return self.success('create done')

class UpdateCourseAPI(APIView):
    def put(self, request):
        data = request.data
        id, name, desc, image, bill, category, teacher_id, detail = data["id"], data["name"], data["desc"], data["image"], data["bill"], data["category"], data["teacher_id"], data["detail"]
        try:
            res = Course.objects.get(id=id)
        except Exception as e:
            return self.error(msg=str(e))

        if name != "":
            cur = Course.objects.filter(name=name)
            if len(cur) > 0: return self.error(msg="name duplicated")
            res.name = name
        if desc != "": res.desc = desc
        if image != "": res.image = image
        if bill != "": res.bill = bill
        if category != "": res.category = category
        if teacher_id != "": res.teacher_id = teacher_id
        if detail != "": res.detail = detail
        res.save()
        return self.success('update done')

class UpdateCourseresourceAPI(APIView):
    def put(self, request):
        data = request.data
        id, name, download, course_id = data["id"], data["name"], data["download"], data["course_id"]
        try:
            res = CourseResource.objects.get(id=id)
        except Exception as e:
            return self.error(msg=str(e))

        if name != "":
            cur = CourseResource.objects.filter(name=name)
            if len(cur) > 0: return self.error(msg="name duplicated")
            res.name = name
        if download != "": res.download = download
        if course_id != "": res.course_id = course_id
        res.save()
        return self.success('update done')

class UpdateLessonAPI(APIView):
    def put(self, request):
        data = request.data
        print(data)
        id, name, course_id, video_id = data["id"], data["name"], data["course_id"], data["video_id"]
        try:
            res = Lesson.objects.get(id=id)
        except Exception as e:
            return self.error(msg=str(e))

        if name != "":
            cur = Lesson.objects.filter(name=name)
            if len(cur) > 0: return self.error(msg="name duplicated")
            res.name = name
        if course_id != "": res.course_id = course_id
        if video_id != "": res.video_id = video_id
        res.save()
        return self.success('update done')

class UpdateCoursetagAPI(APIView):
    def put(self, request):
        data = request.data
        course_id, course_tags = data["course_id"], data["course_tags"]
        res = Course.objects.filter(id=course_id)
        if len(res) == 0: return self.error(msg="cannot find course")
        CourseTag.objects.filter(course_id=course_id).delete()
        for course_tag in course_tags:
            res = CourseTag.objects.create(
                course_id=course_id,
                course_tag=course_tag["name"]
            )
            res.save()
        return self.success('update done')

class DeleteCourseAPI(APIView):
    def delete(self, request):
        data = request.data
        id = data["id"]
        try:
            Course.objects.get(id=id).delete()
        except Exception as e:
            return self.error(msg=str(e))
        return self.success('delete done')

class DeleteCourseresourceAPI(APIView):
    def delete(self, request):
        data = request.data
        id = data["id"]
        try:
            CourseResource.objects.get(id=id).delete()
        except Exception as e:
            return self.error(msg=str(e))
        return self.success('delete done')

class DeleteLessonAPI(APIView):
    def delete(self, request):
        data = request.data
        id = data["id"]
        try:
            Lesson.objects.get(id=id).delete()
        except Exception as e:
            return self.error(msg=str(e))
        return self.success('delete done')

class DeleteCoursestudentAPI(APIView):
    def delete(self, request):
        data = request.data
        id = data["id"]
        try:
            CourseStudent.objects.get(id=id).delete()
        except Exception as e:
            return self.error(msg=str(e))
        return self.success('delete done')

class ResourceDownloadAPI(APIView):
    def get(self, request):
        data = request.data
        id = data["id"]
        res = CourseResource.objects.filter(id=id)
        if len(res) == 0:
            return self.error('result empty')
        file_path = res[0].download
        # print(res[0].download)
        # print(file_path)
        try:
            response = StreamingHttpResponse(open(file_path, 'rb'))
            response['content_type'] = "application/octet-stream"
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
        except Exception as e:
            return self.error('download fail')

class HelloworldAPI(APIView):
    def get(self, request):
        logger.info('hello world')
        #return self.error(err='404', msg='404 not found')
        return self.success('hello world')