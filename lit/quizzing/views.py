from django.shortcuts import render

def home(request):
    return render(request,'quizzing/home.html')

def team(request):
    return render(request,'quizzing/team.html')