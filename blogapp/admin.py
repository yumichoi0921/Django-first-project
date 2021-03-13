from django.contrib import admin
from .models import Blog
from .models import Comment
# Register your models here.

# Blog 모델을 가져오기 위해 Blog를 import하고, admin page에 등록
admin.site.register(Blog)
admin.site.register(Comment)