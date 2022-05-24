from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
'''def logincheck(request):
    username = request.POST['email']
    password = request.POST['password']
    role = request.POST['role']
    user=User.objects.get(email=username)
    if(password==user.user_details['password']):
        return HttpResponse("Login verified")
    else:
        return HttpResponse("Login Failed")
    #return render(request,'logincheck.html',{'username':username,'password':password})'''
