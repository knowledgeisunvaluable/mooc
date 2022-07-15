from django.db import models

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    desc = models.TextField()
    detail = models.TextField()
    learn_times = models.IntegerField()
    students_number = models.IntegerField()
    fav_nums = models.IntegerField()
    image = models.CharField(max_length=100)
    click_nums = models.IntegerField()
    category = models.TextField()
    youneed_know = models.TextField()
    teacher_tell = models.TextField()
    add_time = models.DateTimeField()
    bill = models.IntegerField()
    teacher_id = models.IntegerField()

class CourseResource(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    download = models.CharField(max_length=100)
    add_time = models.DateTimeField()
    course = models.ForeignKey("Course", on_delete=models.CASCADE)

class Lesson(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    add_time = models.DateTimeField()
    course = models.ForeignKey("Course", on_delete=models.DO_NOTHING)
    video_id = models.IntegerField()

class CourseTag(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey("Course", on_delete=models.DO_NOTHING)
    course_tag = models.CharField(max_length=100)

class CourseStudent(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey("Course", on_delete=models.DO_NOTHING)
    student_id = models.IntegerField()