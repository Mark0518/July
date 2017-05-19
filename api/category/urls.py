from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', CategoryView.as_view()),
    url(r'^list/$', CategoryListView.as_view()),
    url(r'^(?P<uid>\d+)/$', CategoryDetailView.as_view()),
]
