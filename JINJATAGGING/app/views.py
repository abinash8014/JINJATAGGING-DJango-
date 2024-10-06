from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.

def home(request):
    users = data.objects.all()
    d = {'users': users}
    return render(request,'home.html',d)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        users = data.objects.all()
        for user in users:
            if user.username == username:
                if user.password == password:
                    d ={'user':user}
                    return render(request,'home.html',d)
                return HttpResponse('Invalid Password')
        else:
            return HttpResponse('User not Found!')
    return render(request,'login.html')


def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        pno = request.POST.get('pno')
        email = request.POST.get('email')
        add = request.POST.get('add')
        username = request.POST.get('username')
        password = request.POST.get('password')
        o1 = data(name=name,pno=pno,email=email,add=add,username=username,password=password)
        o1.save()
        return HttpResponse("Registration Done...")
    return render(request,'register.html')