from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

from .models import User
import bcrypt
# Create your views here.
def index(request):
    return render(request, 'index.html')

def rprocess(request):
    data = {
        "fname": request.POST['fname'],
        "lname": request.POST['lname'],
        "email": request.POST['email'],
        "password": request.POST['password'],
        "cpassword": request.POST['cpassword']
    }
    results = User.objects.validator(data)

    if results[0]:
        request.session['user_id']= results[1].id
        return redirect ("/success")
    else:
        for err in results[1]:
            messages.error(request, err)
        return redirect("/")
def success(request):

    userinsession= User.objects.get(id=request.session['user_id'])

    context={
    "user": userinsession
    }

    return render(request, 'success.html', context)


def login(request):
    data = {
    "email": request.POST['email'],
    "password": request.POST['password'],
    }
    results = User.objects.login(data)

    if results[0]:
        request.session['user_id']= results[1].id
        return redirect ("/success")
    else:
        for err in results[1]:
            messages.error(request, err)

    email = request.POST['email']
    password = request.POST['password']

    if User.objects.filter(email=email):
        user = User.objects.get(email=email)
        if bcrypt.hashpw(password.encode(), user.password.encode()) == user.password:
            return (True, user.id)
        else:
            return (False, "Invalid password")
    else:
        return (False, "Invalid email address")

        return redirect("/")
