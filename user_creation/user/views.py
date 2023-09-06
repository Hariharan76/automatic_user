from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from .models import user_data


def home(request):
    return render(request,"home.html")



def login(request):
    email= request.POST.get('email')
    password= request.POST.get('password')
    user=auth.authenticate(username=email,password=password)     
    if user is not None:
        user_data1 = get_object_or_404(user_data, email=email)   
        user_data_dict = {
        'image': user_data1.image,
        'email': user_data1.email,
        'name': user_data1.first_name+" "+user_data1.last_name,
        'user_type':user_data1.user_type.capitalize()
         
        }     
        return render(request,'index.html',user_data_dict)        
    else:
        messages.info(request,"invalid credintials")   
    return render(request,"login.html")


def register(request):
    if request.method == 'POST':
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        image = request.POST.get('image')
        user_type=request.POST.get('user_type')
        username = email
        print(fname,lname,email,password,password1,image,username)

        if password == password1:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already taken")
                return redirect('register')
            
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return redirect('register')
            else:               
                user = User.objects.create_user(username=username, first_name=fname, last_name=lname, email=email, password=password)
                user.save()    
                user1=user_data()
                user1.first_name=fname
                user1.last_name=lname
                user1.password=password
                user1.email=email
                user1.image=image   
                user1.user_type=user_type       
                user1.save()
                
                return redirect('login')
        else:
            messages.info(request, "Passwords do not match")
    
    return render(request, "register.html")

def index(request):
    
    return render(request,"index.html")
