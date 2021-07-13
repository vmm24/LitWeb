from django.contrib import admin
from django.urls import path
from .views import W_EventListView, W_EventDetailView, D_EventListView, D_EventDetailView, Q_EventListView, Q_EventDetailView
from . import views
urlpatterns = [

    path('writing/<int:pk>/', W_EventDetailView.as_view(), name='w_event_detail'),
    path('writing/', W_EventListView.as_view(), name='w_events_list'),
    path('debating/<int:pk>/', D_EventDetailView.as_view(), name='d_event_detail'),
    path('debating/', D_EventListView.as_view(), name='d_events_list'),
    path('quizzing/<int:pk>/', Q_EventDetailView.as_view(), name='q_event_detail'),
    path('quizzing/', Q_EventListView.as_view(), name='q_events_list'),
]
