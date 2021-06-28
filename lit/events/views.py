from django.shortcuts import render
from .models import Events
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# def events(request):
#     return render(request,'events/events.html')

def events(request):
    context = {
    'events': Events.objects.filter(status=1).order_by('-date')
    }
    return render(request,'events/events.html',context)

class EventListView(ListView):
    queryset = Events.objects.filter(status=1).order_by('-date')
    template_name='events/events.html'

class EventDetailView(DetailView):
    model=Events
    template_name = 'events/events_detail.html'

class EventCreateView(LoginRequiredMixin, CreateView):
    model=Events
    fields = ['title', 'content']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)