from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'quiz/quizhome.html')
def team(request):
    return render(request,'quiz/quizteam.html')
