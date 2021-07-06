from django.contrib import admin
from django.urls import path
from .views import DEventListView, DEventDetailView
from . import views
urlpatterns = [
    path('<int:pk>/', DEventDetailView.as_view(), name='details'),
    path('', views.d_events, name='debate_events-d_events'),
]


# from django.contrib import admin
# from django.urls import path
# # from .views import EventListView, EventDetailView, EventCreateView, EventUpdateView, EventDeleteView
# from .views import EventListView, EventDetailView
# from . import views
# urlpatterns = [

#     path('<int:pk>/', EventDetailView.as_view(), name='event_detail'),
#     path('', EventListView.as_view(), name='events_list'),
# ]

