from django.contrib import admin
from django.urls import path
# from .views import EventListView, EventDetailView, EventCreateView, EventUpdateView, EventDeleteView
from .views import EventListView, EventDetailView, EventCreateView
from . import views
urlpatterns = [
    # path('', views.home, name='blog-home'),
    # path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    # path('events/new/', EventsCreateView.as_view(), name='Event-create'),
    # path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    # path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('events/', EventListView.as_view(), name='events-events'),
    # path('events/', views.events, name='events-events')
]
