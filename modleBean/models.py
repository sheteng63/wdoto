from django.db import models
import json


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    authorId = models.CharField(max_length=20, null=True)
    date = models.DateTimeField(auto_now_add=True)
    pageViews = models.IntegerField(null=True)
    favorite = models.IntegerField(null=True)


# 浏览记录
class BlogView(models.Model):
    userId = models.CharField(max_length=20)
    blogId = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)


#  收藏记录
class BlogFavorite(models.Model):
    userId = models.CharField(max_length=20)
    blogId = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)

# 头像
class AccountImage(models.Model):
    userId = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='upload/%Y/%m/%d')


# 评论
class BlogRemark(models.Model):
    userId = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    remark = models.TextField()
    blogId = models.CharField(max_length=20)
    remarkId = models.CharField(max_length=20, null=True)
