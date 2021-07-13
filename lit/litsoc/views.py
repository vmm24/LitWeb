from django.shortcuts import render
def home(request):
    return render(request,'litsoc/home.html')
# Create your views here.

def secys(request):
    return render(request,'litsoc/mainteam.html')