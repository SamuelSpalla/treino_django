from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Base.as_view()),
    path('home/',views.Home.as_view()),
    path('alternative/',views.Alternative.as_view()),
    
]
