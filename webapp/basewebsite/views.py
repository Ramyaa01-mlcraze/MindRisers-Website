from django.shortcuts import render

# Create your views here.
def baseHome(request):
    return render(request,'baseHome.html')
def aboutus(request):
    return render(request,'aboutus.html')
def register(request):
    return render(request,'register.html')
def login(request):
    return render(request,'login.html')
