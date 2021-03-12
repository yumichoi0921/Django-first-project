"""firstProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
# 현재 Django 프로젝트의 URL을 설정

from django.contrib import admin
from django.urls import path
# 생성한 뷰를 url로 연결하기 위해
# ex. index()를 사용하기 위해 index()가 위치한 view.py를 import
import blogapp.views
from django.conf.urls import include
# MEDIA 경로를참조
from django.conf import settings
from django.conf.urls.static import static
#  path(route, view, kwargs=None, name=None)
urlpatterns = [
    path('admin/', admin.site.urls), # http://www.블로그주소.com/admin 으로 접속
    path('', blogapp.views.index, name='index'), # http://www.블로그주소.com/ 으로 접속
    path('blogMain/', blogapp.views.blogMain, name = 'blogMain'),# http://www.블로그주소.com/blogMain/ 으로 접속
    path('blogMain/createBlog/', blogapp.views.createBlog, name = 'createBlog'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

# MEDIA 경로를참조
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)