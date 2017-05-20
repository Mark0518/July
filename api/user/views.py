from datetime import timedelta

from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.authentication import TokenAuthentication
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
    'RestPasswordView',
    'CodeView'
]


# Create your views here.

class RegisterView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request):
        pp = self.serializer_class(data=request.data)
        if pp.is_valid():
            email = pp.validated_data['email']
            password = pp.validated_data['password']
            code = pp.validated_data['code']
            code = EmailCaptchaCode.objects.get(code=code, status=True, send_time__lt=timezone.now() + timedelta(minutes=CODE_LIFETIME))
            code.status = False
            code.save()
            if code.email == email:
                UserProfile.objects.create(username=email, email=email, password=make_password(password))
                return Response(status=status.HTTP_201_CREATED)
            else:
                raise APIException(code=400, detail='Verification code error!')
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
                if not has_created:
                    Token.objects.filter(user=user).update(key=token.generate_key(), created=timezone.now())
                token = Token.objects.get(user=user)
                return Response({'token': token.key})
            else:
                raise APIException(code=401, detail='Wrong user name or password!')
        else:
            raise APIException(code=400, detail=pp.errors)


class LogOutView(APIView):
    authentication_classes = (TokenAuthentication, BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        request.user.auth_token.delete()
        return Response()


class RestPasswordView(APIView):
    authentication_classes = (TokenAuthentication, BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = RestPasswordSerializer

    def put(self, request):
        pp = self.serializer_class(data=request.data)
        if pp.is_valid():
            user = request.user
            password = pp.validated_data['password']
            code = EmailCaptchaCode.objects.get(code=pp.validated_data['code'], status=True, send_time__lt=timezone.now() + timedelta(minutes=CODE_LIFETIME))
            code.status = False
            code.save()
            is_user = authenticate(username=request.user.email, password=password)
            if is_user:
                return Response(status=status.HTTP_202_ACCEPTED)
            if code.email == user.email:
                user.set_password(raw_password=password)
                user.save()
                request.user.auth_token.delete()
                return Response()
            else:
                raise APIException(code=400, detail='Verification code error!')
        else:
            raise APIException(code=400, detail=pp.errors)


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
