from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import json
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes


def userLogin(request):
    resp = {'code': 0, 'msg': '0'}
    username = request.POST['username']
    password = request.POST['pwd']
    print('login %s' % username)
    user = authenticate(username=username, password=password)
    if user is not None:
        token = Token.objects.get(user=user)
        print('token ' + token.key)
        print('user %s' % user.id)
        resp['token'] = str(token.key)
    else:
        resp['code'] = 1
    return HttpResponse(json.dumps(resp), content_type="application/json")

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def userLogout(request):
    resp = {'code': 0, 'msg': ''}
    uer = request.user
    print("user   %s" % uer.id)
    return HttpResponse(json.dumps(resp), content_type="application/json")


def userCreate(request):
    resp = {'code': 0, 'msg': ''}
    username = request.POST['username']
    email = request.POST['email']
    pwd = request.POST['pwd']
    user = User.objects.create_user(username, email, pwd)
    user.save()
    resp['code'] = 0
    resp['msg'] = "创建成功"
    Token.objects.create(user=user)
    return HttpResponse(json.dumps(resp), content_type="application/json")
