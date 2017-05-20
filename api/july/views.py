from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

__all__ = [
    'LinksView',
    'LinkListView',
    'LinkDetailView',
    'SettingsView',
    'DashboardView'
]


# Create your views here.

class LinksView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        return Response()


class LinkListView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        return Response()


class LinkDetailView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        return Response()


class SettingsView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        return Response()


class DashboardView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        return Response()
