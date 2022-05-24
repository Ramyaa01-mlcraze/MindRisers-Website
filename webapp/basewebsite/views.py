from django.http import HttpResponse
from django.shortcuts import render
from .models import TeacherDetails, User


# Create your views here.
def baseHome(request):
    return render(request,'baseHome.html')
def aboutus(request):
    return render(request,'aboutus.html')
def register(request):
    return render(request,'register.html')
def login(request):
    return render(request,'login.html')
def register_teacher(request):
    return render(request,'register-teacher.html')
def register_student(request):
    return render(request,'register-student.html')
def logincheck(request):
    username = request.POST['email']
    password = request.POST['password']
    role = request.POST['role']
    res=TeacherDetails.objects.all()
    for r in res:
        if(r.email==username):
            if(r.password==password):
                return HttpResponse("Login successful")
def register_student_db(request):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    middlename = request.POST['middlename']
    email = request.POST['email']
    password = request.POST['password']
    study = request.POST['study']
    YOP = request.POST['YOP']
    number = request.POST['number']
    CGPA = request.POST['CGPA']
    College = request.POST['College']
    City = request.POST['City']
    State = request.POST['State']
    branch = request.POST['branch']
    Interest = request.POST['Interest']
    reg = User(firstname = firstname,lastname=lastname,middlename =middlename,email=email,password=password,study=study,YOP=YOP,number=number,CGPA=CGPA,College=College,City=City,State=State,branch=branch,Interest=Interest)
    reg.save()
    return HttpResponse("Registration Done")
def register_teacher_db(request):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    middlename = request.POST['middlename']
    email = request.POST['email']
    password = request.POST['password']
    qual = request.POST['qual']
    pnumber = request.POST['pnumber']
    experience = request.POST['experience']
    city = request.POST['city']
    state = request.POST['state']
    dept = request.POST['dept']
    Specialization = request.POST['Specialization']
    display_name = request.POST['display_name']
    reg = TeacherDetails(firstname = firstname,lastname=lastname,middlename =middlename,email=email,password=password,qual=qual,pnumber=pnumber,experience=experience,city=city,state=state,dept=dept,Specialization=Specialization,display_name=display_name)
    reg.save()
    return HttpResponse("Registration Done")

