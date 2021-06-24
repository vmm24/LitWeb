from django.shortcuts import render
from .models import Events
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# def events(request):
#     return render(request,'events/events.html')

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