from datetime import timedelta

from django.contrib.auth import authenticate
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.utils import timezone
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.static import CODE_LIFETIME
from user.models import EmailCaptchaCode
from user.models import UserProfile
from utils.common_Utils import random_code
from .serializers import *

__all__ = [
    'RegisterView',
    'LogInView',
    'LogOutView',
    # 'PasswordView'
    'CodeView'
]


class CustomBackend(ModelBackend):
    """自定义auth验证，可以通过用户名邮箱登录"""

    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))  # 通过用户名或邮箱获取用户是否存在
            if user.check_password(password):  # 如果用户密码正确返回user对象
                return user
            else:  # 出错或者用户密码错误就返回None
                return None
        except Exception:
            return None


# Create your views here.

class RegisterView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request):
        pp = self.serializer_class(data=request.data)
        if pp.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            retype_password = request.POST.get('retype_password')
            if password == retype_password:
                UserProfile.objects.create(username=email, email=email, password=make_password(password))
                return Response(status=status.HTTP_201_CREATED)
            else:
                raise APIException(code=400, detail='Two passwords are inconsistent!')
        else:
            raise APIException(code=400, detail=pp.errors)


class LogInView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LogInSerializer

    def get(self, request):
        pp = self.serializer_class(data=request.GET)
        if pp.is_valid():
            email = pp.validated_data['email']
            password = pp.validated_data['password']
            user = authenticate(username=email, password=password)
            if user:
                token, has_created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})
            else:
                raise APIException(code=401, detail='Wrong user name or password!')
        else:
            raise APIException(code=400, detail=pp.errors)


class LogOutView(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        request.user.auth_token.delete()
        return Response()


class CodeView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        if 'email' not in request.data:
            raise APIException(code=400, detail='Email field is not filled！')
        email = request.data['email']
        codes = EmailCaptchaCode.objects.filter(email=email).filter(status=True).filter(send_time__lt=timezone.now() + timedelta(minutes=CODE_LIFETIME))
        if codes:
            code = codes.first()
        else:
            code = EmailCaptchaCode.objects.create(email=email, code=random_code())
        return Response({'code': code.code}, status=status.HTTP_201_CREATED)
