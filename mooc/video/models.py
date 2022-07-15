from django.db import models

class Video(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    url = models.TextField()
    learn_times = models.IntegerField(default=0, verbose_name="")
    add_time = models.DateTimeField()