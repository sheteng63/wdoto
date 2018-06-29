from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import json

resp = {'code': 0, 'msg': '', 'data': ''}


def userLogin(request):
    try:
        username = request.POST['username']
        password = request.POST['pwd']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            resp['code'] = 0
            resp['msg'] = '登录成功'
        else:
            resp['code'] = 1
            resp['msg'] = '登录失败'
    except:
        resp['code'] = 1
        resp['msg'] = '登录失败'
        pass
    finally:
        pass

    return HttpResponse(json.dumps(resp), content_type="application/json")


def userLogout(request):
    print(request.session)
    logout(request)
    resp['msg'] = '退出成功'
    return HttpResponse(json.dumps(resp), content_type="application/json")


def userCreate(request):
    username = request.POST['username']
    email = request.POST['email']
    pwd = request.POST['pwd']
    user = User.objects.create_user(username, email, pwd)
    user.save()
    resp['msg'] = "创建成功"
    return HttpResponse(json.dumps(resp), content_type="application/json")
