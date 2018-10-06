from django import forms #forms model import
from .models import Post #Post model import

class PostForm(forms.ModelForm):

    class Meta: #이 폼을 만들기 위해서 어떤 model이 쓰여야 하는지 장고에 알려주는 구문
        model = Post
        #fields = '__all__' #모든 필드 적용시
        fields = ('title', 'text',) # 튜플로 title, text 만 보여지게함.
#이후에는 링크, URL, 뷰 그리고 템플릿을 생성 필요
#1.base.html에 폼과 페이지 링크 : 추가 <a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
#2.urls.py : 추가 url(r'^post/new/$', views.post_new, name='post_new'),
#3.views.py
#4.post_edit.html 파일을 생성해 폼이 작동할 수 있게함
#5.views.py 에서 폼 저장하기
