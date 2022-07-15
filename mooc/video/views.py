from video.serializers import VideoSerializer
from video.models import Video
from course.models import Lesson

from utils.api import APIView

import django.utils.timezone as timezone
import logging

logger = logging.getLogger('mdjango')

class GetVideoAPI(APIView):
    def get(self, request):
        data = request.data
        id = data["id"]
        res = Video.objects.filter(id=id)
        return self.success(self.paginate_data(request, res, VideoSerializer))

class GetVideoByLessonAPI(APIView):
    def get(self, request):
        data = request.data
        lesson_id = data["lesson_id"]
        res = Lesson.objects.filter(id=lesson_id)
        if len(res) == 0: return self.error(msg="cannot find lesson")
        video_id = res[0].video_id
        res = Video.objects.filter(id=video_id)
        if len(res) == 0: return self.error(msg="cannot find video")
        return self.success(self.paginate_data(request, res, VideoSerializer))

class GetVideoByNameAPI(APIView):
    def get(self, request):
        data = request.data
        name = data["name"]
        res = Video.objects.filter(name=name)
        if len(res) == 0: return self.error(msg="cannot find video")
        return self.success(self.paginate_data(request, res, VideoSerializer))

class PostVideoAPI(APIView):
    def post(self, request):
        data = request.data
        name, url, learn_times = data["name"], data["url"], data["learn_times"]
        if name == "": return self.error(msg="name cannot be null")
        if url == "": return self.error(msg="url cannot be null")
        res = Video.objects.filter(name=name)
        if len(res) > 0: return self.error(msg="name duplicated")
        if learn_times == "": learn_times = 0
        res = Video.objects.create(
            name=name,
            add_time=timezone.now(),
            url=url,
            learn_times=learn_times,
        )
        res.save()
        return self.success('create done')

class UpdateVideoAPI(APIView):
    def put(self, request):
        data = request.data
        id, name, url, learn_times = data["id"], data["name"], data["url"], data["learn_times"]
        try:
            res = Video.objects.get(id=id)
        except Exception as e:
            return self.error(msg=str(e))

        if name != "":
            cur = Video.objects.filter(name=name)
            if len(cur) > 0: return self.error(msg="name duplicated")
            res.name = name
        if url != "": res.url = url
        if learn_times != "": res.learn_times = learn_times
        res.save()
        return self.success('update done')

class DeleteVideoAPI(APIView):
    def delete(self, request):
        data = request.data
        id = data["id"]
        try:
            Video.objects.get(id=id).delete()
        except Exception as e:
            return self.error(msg=str(e))
        return self.success('delete done')