from django.db import models
import json

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=30)
    ltitle = models.CharField(max_length=30,null=True)
    body = models.CharField(max_length=20000)
    author = models.CharField(max_length=20,null=True)
    date = models.DateTimeField(auto_now_add=True)
    pageViews = models.IntegerField(null=True)
    favorite = models.IntegerField(null=True)
    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))
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