from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),
    path('members/', views.member_only ),
    path('login/', views.MyTokenObtainPairView.as_view()),
    path('products/', views.Product_view.as_view()),
    path('categories/', views.Category_view.as_view()),
]
