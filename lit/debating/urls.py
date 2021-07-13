from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='debating-home'),
    path('team/', views.team, name='debating-team'),

]