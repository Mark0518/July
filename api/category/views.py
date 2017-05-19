from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *

__all__ = [
    'CategoryView',
    'CategoryListView',
    'CategoryDetailView'
]


# Create your views here.

class CategoryView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        categorys = []
        for category in Category.objects.all():
            categorys.append({'id': category.pk, 'name': category.name, 'article_count': category.article_count()})
        return Response(categorys)


class CategoryListView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = CategoryListSerializer

    def get(self, request):
        categorys = []
        for tag in Category.objects.all():
            categorys.append(self.serializer_class(tag).data)
        return Response(categorys)

    def post(self, request):
        pp = CategoryModelSerializer(data=request.data)
        if pp.is_valid():
            pp.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            raise APIException(code=400, detail=pp.errors)


class CategoryDetailView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = CategoryDetailSerializer

    def get(self, request, uid):
        return Response(self.serializer_class(get_object_or_404(Category, pk=uid)).data)

    def put(self, request, uid):
        print(request.data)
        category = get_object_or_404(Category, pk=uid)
        pp = CategoryModelSerializer(data=request.data)
        if pp.is_valid():
            category.__dict__.update(pp.validated_data)
            category.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            raise APIException(code=400, detail=pp.errors)
