from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *

__all__ = [
    'TagView',
    'TagListView',
    'TagDetailView'
]


# Create your views here.

class TagView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        return Response(list(Tag.objects.values('id', 'name')))


class TagListView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = TagListSerializer

    def get(self, request):
        tags = []
        for tag in Tag.objects.all():
            tags.append(self.serializer_class(tag).data)
        return Response(tags)

    def post(self, request):
        pp = TagModelSerializer(data=request.data)
        if pp.is_valid():
            pp.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            raise APIException(code=400, detail=pp.errors)


class TagDetailView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = TagDetailSerializer

    def get(self, request, uid):
        return Response(self.serializer_class(get_object_or_404(Tag, pk=uid)).data)

    def put(self, request, uid):
        tag = get_object_or_404(Tag, pk=uid)
        pp = TagModelSerializer(data=request.data)
        if pp.is_valid():
            tag.__dict__.update(pp.validated_data)
            tag.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            raise APIException(code=400, detail=pp.errors)
