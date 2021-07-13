from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='quiz-home'),
    path('team/', views.team, name='quiz-team')
]