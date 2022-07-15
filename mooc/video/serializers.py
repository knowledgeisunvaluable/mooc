import datetime
import time

from rest_framework import serializers

class VideoSerializer(serializers.Serializer):
    name = serializers.CharField()
    url = serializers.CharField()
    learn_times = serializers.IntegerField()
    add_time = serializers.DateTimeField()