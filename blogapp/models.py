from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here. ->데이터베이스 설계

class Blog(models.Model):
    # CharField: 문자로 구성되어 있는 항목
    title = models.CharField(max_length=100)
    auto_now_add = True
    # 'auto_now_add=True'->작성자가 값을 입력하지 않아도 현재 시간에 맞춰서 입력
    pub_date = models.DateTimeField(auto_now_add=True)
    # ForeignKey->다대일 관계, User 테이블의 PrimaryKey를 참조
    # [Users]에 등록된 관리자 계정 정보를 가져오고 이 값을 바탕으로 author 항목 설정
    # User 테이블에서 값이 삭제되면 author 항목도 영향을 받아 삭제됨
    # 기본값을 관리자 계정으로 설정
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=1)
    body = RichTextUploadingField()

# 댓글을 위한 model
class Comment(models.Model):
    # [Blog] 모델의 PrimaryKey를 ForeignKey로 참조
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_user = models.TextField(max_length=20)
    comment_thumbnail_url = models.TextField(max_length=300)
    comment_textfield = models.TextField()