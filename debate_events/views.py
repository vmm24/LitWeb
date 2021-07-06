from django.shortcuts import render
from .models import DEvents
from django.views.generic import ListView, DetailView

# Create your views here.
def d_events(request):
    context = {
    'events': DEvents.objects.all()
    }
    return render(request,'debate_events/d_events.html')

class DEventListView(ListView):
    queryset = DEvents.objects.all()
    template_name='debate_events/d_events.html'

class DEventDetailView(DetailView):
    model=DEvents
    template_name = 'debate_events/details.html'





# def events(request):
#     context = {
#     'events': Events.objects.all()
#     }
#     return render(request,'events/events.html',context)

# class EventListView(ListView):
#     queryset = Events.objects.all()
#     template_name='events/events.html'

# class EventDetailView(DetailView):
#     model=Events
#     template_name = 'events/event_detail.html'

