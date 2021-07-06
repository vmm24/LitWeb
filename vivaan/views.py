from django.shortcuts import render
from .models import Mags
from django.views.generic import ListView

def mags(request):
    context = {
    'mags': Mags.objects.all()
    }
    return render(request,'vivaan/magazines.html',context)

class MagListView(ListView):
    queryset = Mags.objects.all()
    template_name='vivaan/mags.html'