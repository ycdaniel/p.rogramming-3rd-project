from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'blog.views.index'),
    url(r'^new/$', 'blog.views.new'),
    url(r'^(?P<pk>\d+)/$', 'blog.views.detail'),
    url(r'^about/$', 'blog.views.about'),
    url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/$', 'blog.views.sum_xy'),
    url(r'^signup/joke/$', 'blog.views.signup_joke'),
]
