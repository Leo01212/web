from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.shortcuts import render, redirect

from .models import table,people
def index(request):
    ob=table.objects.all()
    obj=people.objects.all()
    return render(request,'index.html',{'res':ob,'re':obj})

def reg(request):

    if request.method=='POST':
        un=request.POST['un']
        fn = request.POST['fn']
        ln = request.POST['ln']
        mail = request.POST['mail']
        pw = request.POST['pw']
        cpw = request.POST['cpw']

        if pw==cpw:
            if User.objects.filter(username=un).exists():
                messages.info(request,"user taken")
                return redirect('/register')
            elif User.objects.filter(email=mail).exists():
                messages.info(request,"email taken")
                return redirect('/register')

            else:
                a=User.objects.create_user(username=un,password=pw,first_name=fn,last_name=ln,email=mail)
                a.save()
                return redirect('/login')

        else:
            messages.info(request,"incorrect password")
            return redirect('/register')

    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        un=request.POST['un']
        pw=request.POST['pw']
        user=auth.authenticate(username=un,password=pw)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid creditionals")

    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')