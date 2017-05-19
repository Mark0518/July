from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^register/$', RegisterView.as_view()),
    url(r'^login/$', LogInView.as_view()),
    url(r'^logout/$', LogOutView.as_view()),
    url(r'^code/$', CodeView.as_view()),
]
