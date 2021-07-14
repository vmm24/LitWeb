from django.shortcuts import render
from .models import Events
from django.views.generic import ListView, DetailView

def w_events(request):
    context0 = {
    'w_events': Events.objects.filter(status=0).order_by('-date')
    }
    return render(request,'events/w_events.html',context0)

def d_events(request):
    context1 = {
    'd_events': Events.objects.filter(status=1).order_by('-date')
    }
    return render(request,'events/d_events.html', context1)

def q_events(request):
    context2 = {
    'q_events': Events.objects.filter(status=2).order_by('-date')
    }
    return render(request,'events/q_events.html',context2)

class W_EventListView(ListView):
    queryset = Events.objects.filter(status=0).order_by('-date')
    template_name='events/w_events.html'
    context_object_name = 'w_events_list'

class W_EventDetailView(DetailView):
    model=Events
    template_name = 'events/w_event_detail.html'
    

class D_EventListView(ListView):
    queryset = Events.objects.filter(status=1).order_by('-date')
    template_name='events/d_events.html'
    context_object_name = 'd_events_list'

class D_EventDetailView(DetailView):
    model=Events
    template_name = 'events/d_event_detail.html'
    

class Q_EventListView(ListView):
    queryset = Events.objects.filter(status=2).order_by('-date')
    template_name='events/q_events.html'
    context_object_name = 'q_events_list'
    
class Q_EventDetailView(DetailView):
    model=Events
    template_name = 'events/q_event_detail.html'
    
