from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'blog.views.index'),
    url(r'^(?P<pk>\d+)/$', 'blog.views.detail'),
    url(r'^about/$', 'blog.views.about'),
    url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/$', 'blog.views.sum_xy'),
]
