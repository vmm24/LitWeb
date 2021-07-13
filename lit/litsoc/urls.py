from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='litsoc-home'),
    path('team/', views.secys, name='litsoc-team'),
]