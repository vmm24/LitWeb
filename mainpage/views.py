from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'mainpage/firstpage.html')

def team(request):
    return render(request,'mainpage/mainteam.html')
