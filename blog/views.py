from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import Post

#뷰(view)는 모델과 템플릿을 연결하는 역할을 함.
#post_list 를 뷰에서 보여주고 이를 템플릿에 전달하기 위해서는, 모델을 가져와야 합니다.
#일반적으로 뷰가 템플릿에서 모델을 선택하도록 만들어야 합니다

# post_list 라는 함수( def ) 만들어 요청(request) 을 넘겨받아  render 메서드를 호출합니다. 이 함수는 호출하여 받은(return)  blog/post_list.html 템플릿을 보여줍니다
def post_list(request):
    # posts QuerySet : 쿼리셋(QuerySet)은 전달받은 모델의 객체 목록, 데이터베이스로부터 데이터를 읽고, 필터를 걸거나 정렬을 할 수 있음.
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')#__lte : --2개 사용, lte(less then equal : <=), lt(less then : <), gt(greater than : >), gte(greater than equal : >=)
    return render(request, 'blog/post_list.html', {'posts': posts}) # posts QuerySet을 템플릿 컨텍스트에 전달
 # render 함수에는 매개변수 request (사용자가 요청하는 모든 것)와 'blog/post_list.html' 템플릿이 있습니다.
 # {} 이 보일 텐데, 이곳에 템플릿을 사용하기 위해 매개변수를 추가할 거에요. (이 매개변수를 'posts' 라고 할거에요)
 # {'posts': posts} 이렇게 작성할거에요.  : 이전에 문자열이 와야하고, 작은 따옴표 '' 를 양쪽에 붙이는 것을 잊지 마세요.

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
