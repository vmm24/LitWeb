from django.shortcuts import render
def home(request):
    return render(request,'debating/home.html')
# Create your views here.
def team(request):
    return render(request,'debating/team.html')
