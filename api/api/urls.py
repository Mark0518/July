from django.conf.urls import url, include

from article.views import ArticlesView
from category.views import CategorysView
from july.views import LinksView
from tag.views import TagsView

urlpatterns = [
    url(r'^tags/$', TagsView.as_view()),
    url(r'^categorys/', CategorysView.as_view()),
    url(r'^articles/', ArticlesView.as_view()),
    url(r'^links/', LinksView.as_view()),
    url(r'^auth/', include('user.urls')),
    url(r'^admin/', include('july.urls')),
]
