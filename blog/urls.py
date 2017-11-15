from django.conf.urls import url

from .views import BlogHomeListView, article_detail, article_create, article_delete, article_update

app_name = 'blog'

urlpatterns = [
    url(r'^$', BlogHomeListView.as_view(), name="blog-home"),
    url(r'^(?P<pk>\d+)/$', article_detail, name="article-detail"),
    url(r'^create/$', article_create, name="article-create"),
    url(r'^delete/(?P<pk>\d+)/$', article_delete, name="article-delete"),
    url(r'^update/(?P<pk>\d+)/$', article_update, name="article-update"),
]