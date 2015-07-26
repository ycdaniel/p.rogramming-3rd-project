from django.shortcuts import get_object_or_404, render
from blog.models import Post


def index(request):
    post_list = Post.objects.all()
    return render(request, "blog/index.html", {
        'post_list': post_list,
    })


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_detail.html", {
        'post': post,
    })


def about(request):
    return render(request, "blog/about.html")


def sum_xy(request, x, y):
    result = int(x) + int(y)
    return render(request, "blog/sum_xy.html", {
        'x': x,
        'y': y,
        'result': result,
    })
