from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *

__all__ = [
    'ArticleView',
    'ArticleListView',
    'ArticleDetailView'
]


# Create your views here.

class ArticleView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        return Response(list(Article.objects.values('id', 'name')))


class ArticleListView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = ArticleListSerializer

    def get(self, request):
        articles = []
        for article in Article.objects.all():
            articles.append(self.serializer_class(article).data)
        return Response(articles)

    def post(self, request):
        pp = ArticleModelSerializer(data=request.data)
        if pp.is_valid():
            pp.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            raise APIException(code=400, detail=pp.errors)


class ArticleDetailView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = ArticleDetailSerializer

    def get(self, request, uid):
        return Response(self.serializer_class(get_object_or_404(Article, pk=uid)).data)

    def put(self, request, uid):
        Article = get_object_or_404(Article, pk=uid)
        pp = ArticleModelSerializer(data=request.data)
        if pp.is_valid():
            Article.__dict__.update(pp.validated_data)
            Article.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            raise APIException(code=400, detail=pp.errors)
