from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from blog.models import Post


def index(request):
    post_list = Post.objects.all()
    return render(request, "blog/index.html", {
        'post_list': post_list,
    })


@csrf_exempt
def new(request):
    print("---- new ----")
    print("request.GET = {}".format(request.GET))
    print("request.POST = {}".format(request.POST))
    print("request.FILES = {}".format(request.FILES))

    if request.method == 'POST':
        if 'title' not in request.POST:
            return HttpResponseBadRequest('제목을 지정해주세요.')
        if not request.POST['title']:
            return HttpResponseBadRequest('제목이 비었어요.')

        if 'content' not in request.POST:
            return HttpResponseBadRequest('내용을 지정해주세요.')
        if not request.POST['content']:
            return HttpResponseBadRequest('내용이 비었어요.')

        title = request.POST['title']
        content = request.POST['content']
        post = Post(title=title, content=content)
        post.save()

    return render(request, "blog/form.html")


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
