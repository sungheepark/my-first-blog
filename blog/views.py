from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect

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
    #Post.objects.get(pk=pk) : 블로그 게시글 한 개만 보려면 Post.objects.get(pk=pk) 쿼리셋(queryset) 생성하면됨.
    post = get_object_or_404(Post, pk=pk) #but, Post를 찾지 못하면, 오류 페이지( 페이지 찾을 수 없음 404 : Page Not Found 404) 를 보여줄
    return render(request, 'blog/post_detail.html', {'post': post})

# 폼을 제출할 때, 같은 뷰를 불러옵니다. 이때  request 에는 우리가 입력했던 데이터들을 가지고 있는데,
# request.POST 가 이 데이터를 가지고 있습니다. ( POST 는 글 데이터를 "등록하는(posting)"하는 것을 의미합니다.
# 블로그"글"을 의미하는 "post"와 관련이 없어요) HTML에서 <form> 정의에  method="POST" 라는 속성이 있던 것이 기억나나요?
# 이렇게 POST로 넘겨진 폼 필드의 값들은 이제  request.POST 에 저장됩니다.
# POST 로 된 값을 다른 거로 바꾸면 안 돼요.  method  속성의 값으로 넣을 수 있는 유효한 값 중에  GET 같은 것도 있지만,
# post와 어떤 차이점이 있는지 등에 대해서 다루기에는 너무 길어질 것 같아 생략할게요)
# 이제 view 에서 두 상황으로 나누어 처리해볼게요.
# •첫 번째: 처음 페이지에 접속했을 때입니다. 당연히 우리가 새 글을 쓸 수 있게 폼이 비어있어야겠죠.
# •두 번째: 폼에 입력된 데이터를 view 페이지로 가지고 올 때입니다. 여기서 조건문을 추가시켜야 해요. ( if 를 사용하세요)

@login_required(login_url="admin:login") #파이썬의 장식자 기능. login이 안되어 잇으면 login창으로 이동했다가 다시 넘어옴
def post_new(request):
    if request.method == "POST":   #만약  method 가  POST 라면, 폼에서 받은 데이터를  PostForm 으로 넘겨줌
        form = PostForm(request.POST)
        if form.is_valid():   #품에 들어있는 값들이 올바른지를 확인해야합니다
            post = form.save(commit=False) #commit=False :넘겨진 데이터를 바로 Post모델에 저장하지는 말라는 뜻.작성자를 추가한 다음 저장해야 하니까요
            post.author = request.user
            post.published_date = timezone.now()
            post.save() # post.save() 는 변경사항(작성자 정보를 포함)을 유지할 것이고 새 블로그 글이 만들어질 거에요
            return redirect('post_detail', pk=post.pk) #새 블로그 글을 작성한 다음에  post_detail 페이지로 이동할 수 있으면 좋겠죠
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required(login_url="admin:login") #파이썬의 장식자 기능. login이 안되어 잇으면 login창으로 이동했다가 다시 넘어옴
def post_edit(request, pk): #url로부터 추가로  pk  매개변수를 받아서 처리합니다
    post = get_object_or_404(Post, pk=pk) #수정하고자 하는 글의  Post  모델  인스턴스(instance) 로 가져옵니다
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
