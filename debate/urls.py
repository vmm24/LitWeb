from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='debate-debatehome'),
    path('debateteam/', views.team, name='debate-debateteam'),
]
