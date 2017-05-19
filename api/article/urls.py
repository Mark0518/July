from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', ArticleView.as_view()),
    url(r'^list/$', ArticleListView.as_view()),
    url(r'^(?P<uid>\s+)/$', ArticleDetailView.as_view()),
]
