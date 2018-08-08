from PIL import Image
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import json
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from modleBean.models import AccountImage


def userLogin(request):
    try:
        resp = {'code': 0, 'msg': '0'}
        username = request.POST['username']
        password = request.POST['pwd']
        print('login %s' % username)
        user = authenticate(username=username, password=password)
        if user is not None:
            token = Token.objects.get(user=user)
            resp['token'] = str(token.key)
        else:
            resp['code'] = 1
    except:
        resp['code'] = 1
    finally:
        print(resp)
        return HttpResponse(json.dumps(resp), content_type="application/json")


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def userLogout(request):
    try:
        resp = {'code': 0, 'msg': ''}
        uer = request.user
        print("user   %s" % uer.id)
    except:
        resp['code'] = 1
    finally:
        print(resp)
        return HttpResponse(json.dumps(resp), content_type="application/json")


def userCreate(request):
    try:
        resp = {'code': 0, 'msg': ''}
        username = request.POST['username']
        email = request.POST['email']
        pwd = request.POST['pwd']
        user = User.objects.create_user(username, email, pwd)
        user.save()
        resp['code'] = 0
        resp['msg'] = "创建成功"
        Token.objects.create(user=user)
    except:
        resp['code'] = 1
    finally:
        print(resp)
        return HttpResponse(json.dumps(resp), content_type="application/json")


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def uploadImage(request):
    print("uploadImage")
    resp = {'code': 0, 'msg': ''}
    try:
        img = request.FILES.get('img')
        name = request.FILES.get('img').name
        id = request.user.id
        acc = AccountImage(userId=id, image=img, name=name)
        acc.save()
        scalePic(acc.image)
    except:
        resp['code'] = 1
    finally:
        print(resp)
        return HttpResponse(json.dumps(resp), content_type="application/json")

# 压缩图片
def scalePic(pic):
    image = Image.open(pic)  # 通过cp.picture 获得图像
    width = image.width
    height = image.height
    rate = 1.0  # 压缩率

    # 根据图像大小设置压缩率
    if width >= 2000 or height >= 2000:
        rate = 0.3
    elif width >= 1000 or height >= 1000:
        rate = 0.5
    elif width >= 500 or height >= 500:
        rate = 0.9

    width = int(width * rate)  # 新的宽
    height = int(height * rate)  # 新的高

    image.thumbnail((width, height), Image.ANTIALIAS)  # 生成缩略图
    image.save('media/' + str(pic), 'JPEG')  # 保存到原路径

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def getUserInfo(request):
    resp = {'code': 0, 'msg': ''}
    try:
        data = {}
        id = request.user.id
        AccImg = AccountImage.objects.filter(userId=id).order_by("id")
        data['img'] = str(AccImg[len(AccImg) - 1].image)
        data['name'] = request.user.username
        resp['data'] = data
    except:
        resp['code'] = 1
    finally:
        print(resp)
        return HttpResponse(json.dumps(resp), content_type="application/json")
