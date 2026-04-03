from django.contrib import admin
from django.urls import path
from posts import views

urlpatterns = [
    # path('', views.health , name="health"),
    path('home/', views.home , name="home"),
    path('add_blog/', views.add_blog , name="add_blog"),
    path('delete/<str:id>/', views.delete_blog , name='delete_blog'),
    path('edit/<str:id>/', views.edit_blog , name='edit_blog')
]