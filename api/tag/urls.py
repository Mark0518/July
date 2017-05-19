from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', TagView.as_view()),
    url(r'^list/$', TagListView.as_view()),
    url(r'^(?P<uid>\d+)/$', TagDetailView.as_view()),
]
