from modleBean.models import Blog
from django.http import HttpResponse
from django.forms.models import model_to_dict
import json


# post
def blogAdd(request):
    resp = {'code': 0, 'msg': '0'}
    try:
        title = request.POST["title"]
        ltitle = request.POST["ltitle"]
        body = request.POST["body"]
        author = request.POST["author"]
        pageViews = request.POST["pageViews"]
        favorite = request.POST["favorite"]
        blog = Blog(title=title, ltitle=ltitle, body=body, author=author, pageViews=pageViews, favorite=favorite)
        blog.save()
    except:
        resp['code'] = 1
    finally:
        return HttpResponse(json.dumps(resp), content_type="application/json")


def blogDelete(request):
    resp = {'code': 0, 'msg': '0'}
    try:
        id = request.GET['id']
        blog = Blog.objects.get(id=id)
        blog.delete()
    except:
        resp['code'] = 1
    finally:
        return HttpResponse(json.dumps(resp), content_type="application/json")


def blogUpdate(request):
    pass


def blogList(request):
    resp = {'code': 0, 'msg': '0'}
    try:
        blogs = Blog.objects.all()
        bl = []
        for blog in blogs:
            bl.append(model_to_dict(blog))
        resp['content'] = bl
        print(resp)
    except:
        resp['code'] = 1
    finally:
        return HttpResponse(json.dumps(resp), content_type="application/json")


def blogDetails(request):
    resp = {'code': 0, 'msg': '0'}
    try:
        id = request.GET['id']
        blog = Blog.objects.get(id=id)
        resp['content'] = model_to_dict(blog)
        print(resp)
    except:
        resp['code'] = 1
    finally:
        return HttpResponse(json.dumps(resp), content_type="application/json")


def blogPageView(request):
    resp = {'code': 0, 'msg': '0'}
    try:
        id = request.GET['id']
        blog = Blog.objects.get(id=id)
        blog.pageViews += 1
        blog.save()
    except:
        resp['code'] = 1
    finally:
        return HttpResponse(json.dumps(resp), content_type="application/json")


def blogFavorite(request):
    resp = {'code': 0, 'msg': '0'}
    try:
        id = request.GET['id']
        blog = Blog.objects.get(id=id)
        blog.favorite += 1
        blog.save()
    except:
        resp['code'] = 1
    finally:
        return HttpResponse(json.dumps(resp), content_type="application/json")
