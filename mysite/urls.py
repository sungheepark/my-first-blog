from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')), #blog.urls 의 내용들을 가져오겠다.따라서 blog 내에 urls.py 만들어야함
]
