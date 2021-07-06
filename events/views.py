from django.shortcuts import render
from .models import Events
from django.views.generic import ListView, DetailView

def events(request):
    context = {
    'events': Events.objects.all()
    }
    return render(request,'events/events.html',context)

class EventListView(ListView):
    queryset = Events.objects.all()
    template_name='events/events.html'

class EventDetailView(DetailView):
    model=Events
    template_name = 'events/event_detail.html'