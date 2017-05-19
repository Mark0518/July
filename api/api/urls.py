from django.conf.urls import url, include

urlpatterns = [
    url(r'^tag/', include('tag.urls')),
    url(r'^category/', include('category.urls')),
    url(r'^auth/', include('user.urls')),
]
