from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'debate/debatehome.html')
def team(request):
    return render(request,'debate/debateteam.html')

