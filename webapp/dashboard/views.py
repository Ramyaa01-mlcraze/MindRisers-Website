from django.http import HttpResponse
from django.shortcuts import render
from .models import TeacherDetails, User

# Create your views here.
def student_dashboard(request):
    return render(request,'student.html')
def teacher_dashboard(request):
    return render(request,'teacher.html')
def logincheck(request):
    username = request.POST['email']
    password = request.POST['password']
    role = request.POST['role']
    if(role=="Teacher"):
        res=TeacherDetails.objects.all()
        for r in res:
            if(r.email==username):
                if(r.password==password):
                    request.session['useremail']=username
                    return render(request,'teacher.html')
    elif(role=="Student"):
        res=User.objects.all()
        for r in res:
            if(r.email==username):
                if(r.password==password):
                    request.session['useremail']=username
                    return render(request,'student.html')
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
    request.session['useremail']=email
    return render(request,'student.html')
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
    reg_teacher = TeacherDetails(firstname = firstname,lastname=lastname,middlename =middlename,email=email,password=password,qual=qual,pnumber=pnumber,experience=experience,city=city,state=state,dept=dept,Specialization=Specialization,display_name=display_name)
    reg_teacher.save()
    request.session['useremail']=email
    return render(request,'teacher.html')