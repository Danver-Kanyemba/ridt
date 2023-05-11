from django.db import models

# Create your models here.

class User(models.Model):
    profile_pic = models.CharField(max_length=200, default="/profilepic")
    phone_number = models.IntegerField(default=0)

class Blog(models.Model):
    create_timestamp = models.DateTimeField("date published")
    update_timestamp = models.DateTimeField("date updated")
    created_by =models.ForeignKey(User)

class Comment(models.Model):
    comment_detail = models.CharField(max_length=200)
    create_timestamp = models.DateTimeField("date published")
    update_timestamp = models.DateTimeField("date updated")
    created_by =models.ForeignKey(User)
    