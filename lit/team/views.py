from django.shortcuts import render
from .models import Events
from django.views.generic import ListView

def w_c_team(request):
    context0 = {
    'w_c_team': Events.objects.filter(club=0).filter(status=0)
    }
    return render(request,'events/w_team.html',context0)

def d_c_team(request):
    context1={
    d_c_team: Events.objects.filter(club=1).filter(status=0)
    }
    return render(request,'events/d_team.html', context1)

def q_c_team(request):
    context2 = {
    'q_c_team': Events.objects.filter(club=2).filter(status=0)
    }
    return render(request,'events/q_team.html',context2)

def w_f_team(request):
    context0 = {
    'w_c_team': Events.objects.filter(club=0).filter(status=1)
    }
    return render(request,'events/w_team.html',context0)

def d_f_team(request):
    context1={
    d_c_team: Events.objects.filter(club=1).filter(status=1)
    }
    return render(request,'events/d_team.html', context1)

def q_f_team(request):
    context2 = {
    'q_c_team': Events.objects.filter(club=2).filter(status=1)
    }
    return render(request,'events/q_team.html',context2)

class W_TeamListView(ListView):
    queryset = Events.objects.filter(status=0).order_by('-date')
    template_name='events/w_events.html'
    context_object_name = 'w_events_list'    

class D_TeamListView(ListView):
    queryset = Events.objects.filter(status=1).order_by('-date')
    template_name='events/d_events.html'
    context_object_name = 'd_events_list'
    
class Q_TeamListView(ListView):
    queryset = Events.objects.filter(status=2).order_by('-date')
    template_name='events/q_events.html'
    context_object_name = 'q_events_list'   
