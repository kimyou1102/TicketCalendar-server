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
        print('0 아니다')
        # if User.objects.filter(user_id=kakao_response['id']).exists():
        #     user = User.objects.get(user_id=kakao_response['id'])
        # else:
        #     return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        user_info = {'user_id': kakao_user_response['id'], 'user_nickname': kakao_user_response['properties']['nickname'], 'age_range': kakao_user_response['kakao_account']['age_range'], 'email': kakao_user_response['kakao_account']['email']}
        print(user_info)
        login_response = login(user_info)
        return login_response

def login(data):
    serializer = UserSerializer(data=data)
    print(serializer)
    if serializer.is_valid():
        user = serializer.save()
        # jwt 토큰 접근
        token = TokenObtainPairSerializer.get_token(user)
        print('token : ', token)
        refresh_token = str(token)
        print('refresh_token : ', refresh_token)
        access_token = str(token.access_token)
        print('access_token : ', access_token)

        res = Response(
            {
                "user": serializer.data,
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
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)