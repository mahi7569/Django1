from django.shortcuts import render,redirect
from .models import Register 

def home(request):
    return render(request,'myapp/home.html') 

def register(request): 
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['paqssword']

        register.objects.create(  
            name=name,
            email=email,
            password=password
        ).save()
        return redirect('home')
    return render(request,'myapp/register.html')   

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']

        if register.objects.filter(email=email,password=password ).exists():  
            return redirect('home')
        else:
            return redirect('register')
    return render(request,'myapp/login.html') 

def ContactUs(request): 
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        mobile=request.POST['mobile']

        ContactUs.objects.create(
            name=name,
            email=email,
            mobile=mobile
        ).save()
        return redirect('home')
    return render(request,'myapp/ContactUs.html')        
  


