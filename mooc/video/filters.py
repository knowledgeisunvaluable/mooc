from django_filters import rest_framework as filters

from video.models import Video

class VideoFilter(filters.FilterSet):
    class Meta:
        model = Video
        fields = "__all__"