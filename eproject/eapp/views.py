from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from . models import *

# Create your views here.
def index(request):
    course=Addregistration.objects.all()
    print(course,'hiiii')
    context={
        'course':course
    }
    return render(request,'index.html',context)
def about(request):
    return render(request,'about.html')

def courses(request,cat):
    print(cat)
    course=Addregistration.objects.filter(coursetype=cat)
    print(course,'hloo')
    context={
        'course':course
    }

    
    return render(request,'courses.html',context)
def contact(request):
    return render(request,'contact.html')

def team(request):
    return render(request,'team.html')

def testimonial(request):
    return render(request,'testimonial.html')
def new(request):
    return render(request,'404.html')
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')
def newdata(request):
    
    if request.method=='POST':
        cname=request.POST.get('courseName')
        mentorname=request.POST.get('mentorName')
        coursefee=request.POST.get('courseFee')
        courserating=request.POST.get('courseRating')
        coursedescription=request.POST.get('courseDescription')
        coursetype=request.POST.get('courseType')
        courseimage=request.FILES.get('courseImage')
        print(cname,mentorname,coursefee,courserating,coursedescription,courseimage,coursetype)
    
        course=Addregistration.objects.filter(coursename=cname)
        if course:
            messages.success(request,"course already exist")
            return redirect('newdata')
        else:
            Addregistration.objects.create(coursename=cname,mentorname=mentorname,coursefee=coursefee,courserating=courserating,coursedescription=coursedescription,courseimage=courseimage,coursetype=coursetype)
            messages.success(request,"created successfully")
            return redirect('index')
    return render(request,'add.html')
def savedata(request):
    if request.method=='POST':
        name=request.POST.get('name')
        lname=request.POST.get('lname')
        age=request.POST.get('age')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpass=request.POST.get('cpass')
        print(name,lname,age,email,password,cpass)
        if password!=cpass:
            messages.error(request,'check your password')
            return redirect('register')
        else:
            Registration.objects.create(name=name,email=email,password=password)
            # Registration(name=name,email=email,password=password).save()
            
            messages.success(request,'account created successfully')
            return redirect('login')
def userdata(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=Registration.objects.filter(email=email,password=password)

    if user:
        return redirect('index')
    else:
        messages.error(request,'invalid email or password')
        return redirect('login')
    
        # print(email,password)
    
    # try: 
    #     check=Registration.objects.get(email=email)
    #     if check:
    #         return redirect('index')
    #     else:
    #         return redirect('login')
    # except:
    #     print('error')
    #     return redirect('login')
    # print(email,password)
    # return redirect('index')
    

        
