from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, UserManager

# Create your views here.

def registration(request):
    if 'user_id' in request.session:
        return redirect('/courts/')
    else:
        return render(request, "/users/registration.html")

def register(request):
    errors = User.objects.validate(request.POST)
    if errors:
        for error in errors:
            messages.error(request, error)
    else:
        User.objects.create_user(request.POST)
    return redirect('/courts/')

def login(request):
    valid, result = User.objects.login(request.POST)
    if not valid:
        messages.error(request,result)
        return redirect('/')
    else:
        request.session['user_id'] = result.id
    return redirect('/courts/court/select')

def logout(request):
    request.session.clear()
    return render(request, '/courts/')
