from django.utils.datastructures import MultiValueDictKeyError

from modleBean.models import Blog, BlogView, BlogFavorite, BlogRemark, AccountImage
from django.http import HttpResponse
from django.forms.models import model_to_dict
import json
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def blogAdd(request):
    resp = {'code': 0, 'msg': '0'}
    try:
        title = request.POST["title"]
        body = request.POST["body"]
        authorId = request.user.id
        pageViews = request.POST.get("pageViews")
        favorite = request.POST.get("favorite")
        if pageViews == None:
            pageViews = 0
        if favorite == None:
            favorite = 0
        blog = Blog(title=title, body=body, authorId=authorId, pageViews=pageViews, favorite=favorite)
        blog.save()
    except MultiValueDictKeyError:
        resp['code'] = 2
        resp['msg'] = '参数缺失'
    except:
        resp['code'] = 1
    finally:
        return HttpResponse(json.dumps(resp), content_type="application/json")


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def blogDelete(request):
    resp = {'code': 0, 'msg': '0'}
    try:
        id = request.POST['id']
        authorId = request.user.id
        blog = Blog.objects.get(id=id)
        if blog == None:
            resp['code'] = 2
            resp['msg'] = '找不到id'

        elif blog.authorId != authorId:
            resp['code'] = 3
            resp['msg'] = "只有作者能删除"
        else:
            blog.delete()
    except MultiValueDictKeyError:
        resp['code'] = 2
        resp['msg'] = '参数缺失'
    except:
        resp['code'] = 1
    finally:
        return HttpResponse(json.dumps(resp), content_type="application/json")


def blogUpdate(request):
    pass


def blogList(request):
    print("blogList")
    resp = {'code': 0, 'msg': '0'}
    try:
        blogs = Blog.objects.all().order_by("-id")
        print(blogs)
        bl = []
        for blog in blogs:
            blogRes = model_to_dict(blog)
            blogRes['date'] = str(blog.date.strftime("%m-%d %H:%I"))
            user = User.objects.get(id=blog.authorId)
            blogRes['authorName'] = user.username
            AccImg = AccountImage.objects.filter(userId=blog.authorId).order_by("-id")
            blogRes['authorImg'] = str(AccImg[0].image)
            bl.append(blogRes)
        resp['content'] = bl
        print(resp)
    except MultiValueDictKeyError:
        resp['code'] = 2
        resp['msg'] = '参数缺失'
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
    except MultiValueDictKeyError:
        resp['code'] = 2
        resp['msg'] = '参数缺失'
    except:
        resp['code'] = 1
    finally:
        return HttpResponse(json.dumps(resp), content_type="application/json")


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def blogPageView(request):
    resp = {'code': 0, 'msg': '0'}
    try:
        id = request.POST['id']
        blog = Blog.objects.get(id=id)
        blog.pageViews += 1
        blog.save()
        blogView = BlogView(userId=request.user.id, blogId=id)
        blogView.save()
    except MultiValueDictKeyError:
        resp['code'] = 2
        resp['msg'] = '参数缺失'
    except:
        resp['code'] = 1
    finally:
        return HttpResponse(json.dumps(resp), content_type="application/json")


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def blogFavorite(request):
    resp = {'code': 0, 'msg': '0'}
    try:
        id = request.POST['id']
        blog = Blog.objects.get(id=id)
        blog.favorite += 1
        blog.save()
        blogFav = BlogFavorite(userId=request.user.id, blogId=id)
        blogFav.save()
    except MultiValueDictKeyError:
        resp['code'] = 2
        resp['msg'] = '参数缺失'
    except:
        resp['code'] = 1
    finally:
        return HttpResponse(json.dumps(resp), content_type="application/json")


# 权限
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def blogRemark(request):
    resp = {'code': 0, 'msg': '0'}
    try:
        blogId = request.POST['blogId']
        userId = request.user.id
        remark = request.POST['remark']
        remarkId = request.POST.get("remarkId")
        blogRemark = BlogRemark(userId=userId, blogId=blogId, remark=remark, remarkId=remarkId)
        blogRemark.save()
    except MultiValueDictKeyError:
        resp['code'] = 2
        resp['msg'] = '参数缺失'
    except:
        resp['code'] = 1
        resp['msg'] = '其他错误'
    finally:
        return HttpResponse(json.dumps(resp), content_type="application/json")


# 权限还没加
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def blogRemarkDel(request):
    resp = {'code': 0, 'msg': '0'}
    try:
        blogId = request.POST['blogId']
        userId = request.user.id
        remarkId = request.POST.get("remarkId")
        blogRemark = BlogRemark.objects.get(userId=userId, id=remarkId, blogId=blogId)
        blogRemark.save()
    except MultiValueDictKeyError:
        resp['code'] = 2
        resp['msg'] = '参数缺失'
    except:
        resp['code'] = 1
        resp['msg'] = '其他错误'
    finally:
        return HttpResponse(json.dumps(resp), content_type="application/json")
