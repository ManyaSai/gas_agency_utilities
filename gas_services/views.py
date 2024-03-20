from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    return(signin(request))

def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST["password"]

        myuser=User.objects.create_user(username,email,password)
        myuser.first_name=fname
        myuser.last_name=lname

        myuser.save()
        messages.success(request,"Your account has been created")

        return redirect('signin')


    return(render(request,"signup.html"))


def signin(request):
    if request.method=="POST":
        username=request.POST['username']
        pass1=request.POST['password']

        user=authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            fname=user.first_name
            print(fname)
            return render(request,'home.html',{"fname":fname})
        else:
            messages.error(request,"Bad Credentials")
            return redirect('signin')


    return(render(request,"signin.html"))

def signout(request):
    logout(request)
    messages.success(request,"Logged out successfully")
    return(redirect("signin"))