from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse
from .models import *

# http response codes
# 200 = OK
# 403 = forbidden
# 409 = conflict

# Create your views here.

# for testing, might delete
def integer(request):
    print(request.POST)


    return HttpResponse(request.POST.get('value'))

# not necessary according to specs so im leaving it as is
def recycle(request):
    print(request.POST)
    return HttpResponse(request.POST.get('value'))

def login(request):
    # check if password given is the same as the password stored
    if(request.POST.get("password") != user.objects.filter(email=request.POST.get("email")).values()[0]["password_sha256"]):
       return HttpResponse(status=403)

    return HttpResponse(request.POST.get('value'))

def register(request):
    print(request.POST)

    # reject request if user already exists
    if(user.objects.filter(email=request.POST.get("email"))):
        return HttpResponse(status=409)


    return HttpResponse(status=200)