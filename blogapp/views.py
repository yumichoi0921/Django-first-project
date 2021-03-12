# 파이썬 문법을 활용하여 여러 함수들을 생성
# 이 함수들을 이용하여 자신이 원하는 형태로 데이터를 처리한 후 탬플릿을 불러오거나 URL로 이동

from django.shortcuts import render, redirect
# form을 createBlog.html로 보내기 위해 import로 불러들임
from .forms import CreateBlog
from  .models import Blog

# Create your views here.

# render(request, template_name, context=None, content_type=None, status=None, using=None)
# 요청(데이터)을 받아서 탬플릿으로 리턴(전달)
# request: 요청을 처리하기 위한 인자
# 탬플릿에 context를 보내고 탬플릿에서 장고 템플릿 변수를 이용하여 값을 출력
# context로 표현된 템플릿의 HttpResponse 객체가 반환됨
# context: 딕셔너리형, view에서 사용하던 파이썬 변수를 html 템플릿으로 넘김
# key값: 탬플릿에서 사용할 변수이름, value값: 파이썬 변수

# redirect(to, permanent=False, *args, **kwargs)
# 단순히 특정 URL 또는 프로젝트 내의 문서로 이동
# to: 이동할 URL, urls.py에 name을 정의하고 이를 많이 사용 (상대 URL, 절대 URL 모두 가능)
# URL로 이동하는 것이기 때문에 render 처럼 context 값을 넘기지는 못함
# URL에 맞는 views가 다시 실행, 여기서 render를 할지 다시 redirect 할지 결정

# render는 템플릿을 불러오고, redirect는 URL로 이동


# 통상적으로 html 문서의 이름과 똑같이 함수의 이름을 지정
def index(request):
    return render(request, 'index.html')

def blogMain(request):

    # 데이터베이스에 저장된 객체를 모두 가리키는 객체 'blogs'를 'blogMain.html'에 보내줌
    blogs = Blog.objects.all()

    return render(request, 'blogMain.html', {'blogs' : blogs})

def createBlog(request):

    # 데이터들이 POST 방식으로 넘어옴->createBlog.html에서 [저장]을 누른 것
    if request.method == 'POST':
        # class CreateBlog(forms.ModelForm)
        # 위 form에 값을 전달한 상태로 [form] 객체를 만듦
        form = CreateBlog(request.POST)
        # form의 데이터들이 올바른 형식-데이터베이스에 저장, 블로그 메인 화면으로 이동
        if form.is_valid():
            form.save()
            return redirect('blogMain')
        else:
            return redirect('index')
    # 데이터들이 POST 방식으로 넘어오지 않음->단순히 [글쓰기] 버튼을 누른 것
    else:
        # 불러들인 form을 createBlog.html로 보내기 위해 객체 생성 후 보냄
        form = CreateBlog()
        return render(request, 'createBlog.html', {'form': form})


