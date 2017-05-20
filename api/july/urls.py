from django.conf.urls import url
from tag.views import *
from category.views import *
from article.views import *
from july.views import *

urlpatterns = [
    url(r'^tags/$', TagListView.as_view()),
    url(r'^tag/(?P<uid>\d+)/$', TagDetailView.as_view()),
    url(r'^categorys/$', CategoryListView.as_view()),
    url(r'^category/(?P<uid>\d+)/$', CategoryDetailView.as_view()),
    url(r'^articles/$', ArticleListView.as_view()),
    url(r'^article/(?P<uid>\d+)/$', ArticleDetailView.as_view()),
    url(r'^links/$', LinkListView.as_view()),
    url(r'^link/(?P<uid>\d+)/$', LinkDetailView.as_view()),
    url(r'^settings/$', SettingsView.as_view()),
    url(r'^dashboard/$', DashboardView.as_view()),
]
