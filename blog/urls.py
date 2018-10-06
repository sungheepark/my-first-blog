from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]
# post/ 란 URL이 post 문자를 포함해야 한다는 것을 말합니다. 아직 할 만하죠?
# (?P<pk>\d+) : 장고가 pk 변수에 모든 값을 넣어 뷰로 전송하겠다는 뜻
# \d 은 문자를 제외한 숫자 0부터 9 중, 한 가지 숫자만 올 수 있다는 것을 말합니다.
# + 는 하나 또는 그 이상의 숫자가 올 수 있습니다..
# 따라서  http://127.0.0.1:8000/post/ 라고 하면 post/ 다음에 숫자가 없으므로 해당 사항이 아니지만,
#  http://127.0.0.1:8000/post/1234567890/ 는 완벽하게 매칭됩니다.
# 브라우저에  http://127.0.0.1:8000/post/5/ 라고 입력하면,
# 장고는  post_detail  뷰를 찾아 매개변수  pk 가  5 인 값을 찾아 뷰로 전달합니다
