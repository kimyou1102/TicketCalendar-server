from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.kakaoLogin, name="kakaoLogin"),
    path('logout/', views.logout, name="logout"),
]