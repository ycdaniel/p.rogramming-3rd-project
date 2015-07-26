
# cheatsheet

## 초기 django 프로젝트 생성
```sh
python manage.py startproject project3
cd project3
```

## 기본 django app 에 대해 migrate
```sh
python manage.py migrate
```

기본 django app 에서는 이미 migrations 파일들이 생성되어있으므로, makemigrations 이 필요없구요. migrate 만 하면 충분합니다.

## superuser 계정 생성
```sh
python manage.py createsuperuser
```

생성된 계정으로, http://localhost:8000/admin/ 에 로그인이 가능합니다. :D

## 최초의 blog 앱 생성
```sh
python manage.py startapp blog
```

## settings 의 INSTALLED_APPS 에 blog 앱 추가
```python
# project3/settings.py
INSTALLED_APPS = (
    # (중략) ...
    'blog',
)
```

INSTALLED_APPS : django 프로젝트 내 관리대상 app 목록

 * 여기에 포함되지 않으면 ...
  * 마이그레이션 대상에서 제외
  * 차후 배울 templates, static loader 대상에서도 제외
  * urls/view 라우팅은 project/urls.py 에서 직접 라우팅하기 때문에, INSTALLED_APPS 에 포함되지 않아도 가능함.

## blog 앱, Post 모델 생성
```python
# blog/models.py 파일
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

### 마이그레이션 적용
```sh
python manage.py makemigrations
python manage.py migrate
```

### admin 에 Post 모델 등록
```python
# blog/admin.py 파일
from django.contrib import admin
from blog.models import Post

admin.site.register(Post)
```

이제 admin 페이지에서 Post 모델 관련 CRUD 작업을 할 수 있습니다. http://localhost:8000/admin/ 에서 Post 데이터를 10개 정도 생성해보세요.

## blog 방문객들이 Post 를 조회할 수 있도록, Post 목록 뷰 작성
```python
# project3/urls.py
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),  ## 추가됨.
]
```

```python
# blog/urls.py
from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'blog.views.index'),
]
```

```python
# blog/views.py
from django.shortcuts import render
from blog.models import Post

def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', {
        'post_list': post_list,
    })
```

```html
<!-- blog/templates/blog/index.html-->
<style>
td {
    border: 1px solid red;
    background-color: lightyellow;
}
</style>

<table>
    {% for post in post_list %}
    <tr>
        <td>{{ post.id }}</td>
        <td>{{ post.title }}</td>
        <td>{{ post.updated_at }}</td>
    </tr>
    {% endfor %}
</table>
```

이제 http://localhost:8000/blog/ 주소를 통해 post 목록을 확인할 수 있습니다.

## blog 방문객들이 각 Post 의 내용을 조회할 수 있도록, Post Detail 뷰 작성

```python
# blog/urls.py
from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'blog.views.index'),
    url(r'^(?P<pk>\d+)/$', 'blog.views.detail'),  # 추가됨.
]
```

```python
# blog/views.py

def detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/detail.html', {
        'post': post,
    })
```

```html
<!-- blog/templates/blog/detail.html -->

<h1>{{ post.title }}</h1>

{{ post.content }}

<hr/>
<a href="/blog/">글 목록</a>
```

이제 http://localhost:8000/blog/1/ 등의 주소를 통해 post 내용을 확인할 수 있습니다.

## post index 템플릿에서 post detail 뷰로의 링크 추가
```html
<!-- blog/templates/blog/index.html-->
<style>
td {
    border: 1px solid red;
    background-color: lightyellow;
}
</style>

<table>
    {% for post in post_list %}
    <tr>
        <td>{{ post.id }}</td>
        <!-- 링크 부분만 추가됨. -->
        <td><a href="/blog/{{ post.id }}/">{{ post.title }}</a></td>
        <td>{{ post.updated_at }}</td>
    </tr>
    {% endfor %}
</table>
```

이제 링크만 눌러도, 각 post 내용을 즉시 확인할 수 있습니다.
