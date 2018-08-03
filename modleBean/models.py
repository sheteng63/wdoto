from django.db import models
import json

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=30)
    ltitle = models.CharField(max_length=30)
    body = models.CharField(max_length=20000)
    author = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)
    pageViews = models.IntegerField()
    favorite = models.IntegerField()
    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))
