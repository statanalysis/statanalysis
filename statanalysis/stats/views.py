from django.shortcuts import render
from django.http import *
from decimal import *
from django.template import loader
from .models import *
from datetime import datetime, timedelta, date
from django.db.models import Sum

# Create your views here.
def home(request):
   
    template=loader.get_template('home.html')
    context ={'r':'r',}
    return HttpResponse(template.render(context,request))

def new(request):
   
    template=loader.get_template('new.html')
    context ={'r':'r',}
    return HttpResponse(template.render(context,request))