from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render
from blog.models import Post
from blog.forms import PostForm


def index(request):
    post_list = Post.objects.all()
    return render(request, "blog/index.html", {
        'post_list': post_list,
    })


def new(request):
    print("---- new ----")
    print("request.GET = {}".format(request.GET))
    print("request.POST = {}".format(request.POST))
    print("request.FILES = {}".format(request.FILES))

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            post = Post(title=title, content=content)
            post.save()
            return redirect('blog.views.index')
    else:
        form = PostForm()

    return render(request, "blog/form.html", {
        'form': form,
    })


def detail(request, pk):
#   try:
#       post = Post.objects.get(pk=pk)
#   except Post.DoesNotExist:
#       raise Http404

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
