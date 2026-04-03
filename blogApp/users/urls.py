from django.contrib import admin
from django.urls import path
from users import views

urlpatterns = [
    path('users/', views.get_users, name="user"),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout")
]