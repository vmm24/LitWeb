from django.contrib import admin
from django.urls import path
from .views import MagListView
from . import views
urlpatterns = [

    path('', MagListView.as_view(), name='mags_list'),
]
