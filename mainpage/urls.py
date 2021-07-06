from django.contrib import admin
from django.urls import path
# from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views
urlpatterns = [
    path('', views.home, name='mainpage-firstpage'),
    path('mainteam/', views.team, name='mainpage-mainteam'),
    # path('events/', views.events, name='blog-events')
]
