# 전에 만든 데이터베이스 모델에서 항목들을 가져오는 작업
# 장고에서 기본적으로 지원하는 forms import

from django import forms
from .models import Blog

# 블로그를 생성->이름 [CreateBlog]
# 장고에서 Meta 클래스는 내부 클래스로 활용, 기본 필드의 값을 재정의할 때 사용
# [Blog]로 부터 모델을 가져오고 그 중 'title', 'author', 'body'를 가져옴
class CreateBlog(forms.ModelForm):
    class Meta:
        model = Blog

        # 'pub_date'는 자동으로 입력이 되게 설정했으므로 뺌
        fields = ['title', 'author', 'body']