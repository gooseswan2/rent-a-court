from django.shortcuts import render,redirect
from django.contrib import messages
from django.template import Context
from .models import Court, CourtManager, SelectedCourt
from apps.users.models import User
from datetime import datetime
from decimal import Decimal
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, "courts/index.html")

def main(request):
    context = {
        'court' : Court.objects.all()
    }
    return render(request, "courts/main.html", context)

def court(request, courtid):
    context = {
        'one_court' : Court.objects.get(id=courtid)
    }
    return render(request, "courts/courts.html", context)

def select(request):
    if 'user_id' not in request.session:
        context = {
            'message' : "Please login"
        }
        return render(request, "courts/index.html", context)
    context = {
        'courts' : Court.objects.all()
    }
    return render(request, "courts/select.html", context)
"""
This is logic that checks the times that a court has been reserved.
"""
def schedule(request):
    if 'user_id' not in request.session:
        context = {
            'message' : "Please login"
        }
        return render(request, "courts/", context) 
    usr = User(id=request.session['user_id'])
    crt = Court.objects.get(id=request.POST['courtid'])
    intime = request.POST['timein']
    outtime = request.POST['timeout']
    dform = "%Y-%m-%d %H:%M"
    diff = datetime.strptime(outtime, dform) - datetime.strptime(intime, dform)
    hours = diff.seconds/3600 
    if hours < 4 and hours > 0:
       total_price = Decimal(hours) * crt.price
       if intime > outtime:
            context = {
                'courts' : Court.objects.all(),
                'message': "End date/time is earlier than begin date/time."
            }
       elif intime <= datetime.now().strftime(dform):
            context = {
                'courts' : Court.objects.all(),
                'message': "Begin date/time is in the past."
            }
       else:
            SelectedCourt.objects.create(user=usr, court=crt, timein=intime, timeout=outtime, total_price=total_price)
            context = {
                'courts' : Court.objects.all()
            }
    else:
       context = {
                'courts' : Court.objects.all(),
                'message': "Scheduled time is too long."
       } 

    return render(request, "courts/select.html", context)
"""
This presents a dashboard which shows court reservations.
"""

def dashboard(request):

    if 'user_id' not in request.session:
        context = {
            'message' : "Please login"
        }
        return render(request, "courts/index.html", context)

    usr = User(id=request.session['user_id'])
    context = {
        'court_times' : SelectedCourt.objects.filter(user=usr)
    }

    return render(request, "courts/dashboard.html", context)

def search(request):
    return render(request, "courts/search.html")

def searchzip(request):
    return "HELLO WORLD"