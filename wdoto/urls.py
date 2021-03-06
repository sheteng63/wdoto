"""wdoto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import view
from . import blog
from django.views.static import serve
from wdoto.settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    url('user/login', view.userLogin),
    url('user/logout', view.userLogout),
    url('user/resgiter', view.userCreate),
    url('user/uploadImg', view.uploadImage),
    url('user/info', view.getUserInfo),

    url('blog/add', blog.blogAdd),
    url('blog/del', blog.blogDelete),
    url('blog/update', blog.blogUpdate),
    url('blog/list', blog.blogList),
    url('blog/details', blog.blogDetails),
    url('blog/pageView', blog.blogPageView),
    url('blog/favorite', blog.blogFavorite),
    url('blog/remark', blog.blogRemark),
    url('blog/remarkDel', blog.blogRemarkDel),

    url(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
]