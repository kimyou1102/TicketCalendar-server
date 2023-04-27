import json
from django.shortcuts import render
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import response

from .models import User
from .serializer import UserSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt import tokens, views as jwt_views, serializers as jwt_serializers, exceptions as jwt_exceptions

from datetime import timedelta
# Create your views here.

@api_view(['POST'])
def kakaoLogin(request):
    kakao_access_code = request.data['access_token']
    url="https://kapi.kakao.com/v2/user/me"
    headers={
                "Authorization":f"Bearer {kakao_access_code}",
                "Content-type":"application/x-www-form-urlencoded; charset=utf-8"
            }
    kakao_response=requests.post(url,headers=headers)
    kakao_user_response=json.loads(kakao_response.text)

    if len(User.objects.all()) != 0:     
        if User.objects.filter(p_id=kakao_user_response['id']).exists():
            user = User.objects.filter(p_id=kakao_user_response['id'])
            serializer = UserSerializer(data=user.values()[0])
            login_response = login(user.values()[0], user[0])
            return login_response
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        user_info = {'p_id': kakao_user_response['id'], 'user_nickname': kakao_user_response['properties']['nickname'], 'age_range': kakao_user_response['kakao_account']['age_range'], 'email': kakao_user_response['kakao_account']['email']}
        serializer = UserSerializer(data=user_info)
        if serializer.is_valid():
            user = serializer.save()
            login_response = login(user_info, user)
            return login_response
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def login(user_obj, user):
    token = TokenObtainPairSerializer.get_token(user)
    refresh_token = str(token)
    access_token = str(token.access_token)
    res = Response(
        {
            "user": user_obj,
            "message": "register successs",
            "token": {
                "access": access_token,
                "refresh": refresh_token,
            },
        },
        status=status.HTTP_200_OK,
    )
    # jwt 토큰 => 쿠키에 저장
    res.set_cookie("access", access_token, httponly=True, samesite=None, secure=True, expires=timedelta(minutes=5)) 
    res.set_cookie("refresh", refresh_token, httponly=True, samesite=None, secure=True, expires=timedelta(minutes=5))
    return res