from django.urls import path
from django.contrib import admin
from . import views
from .views import post_detail
from .views import health_check

urlpatterns = [
      path('', views.home, name="home"),
      path('main/', views.main, name='main'),
      path('section2/', views.section2, name='section2'),
      path('gallery/', views.gallery, name='gallery'),
      path('section4/', views.section4, name='section4'),
      path('section5/', views.section5, name='section5'),
      path('post/<int:post_id>/', post_detail, name='post_detail'),
      path('health/', health_check, name='health_check'),
]