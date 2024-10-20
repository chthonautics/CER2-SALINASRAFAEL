from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .forms import *

from api import models

# Create your views here.

def index(request):
    data = {}

    token = models.user.objects.filter(session_token=request.session.get("token")).values()
    print(token)
    print(request.session.get("token"))

    if request.POST:
        print(request.POST.get(''))

    return render(request, 'index.html', data)

def store(request):
    data = {}

    return render(request, 'store.html', data)

def form(request):
    data = {'form': recycle()}

    return render(request, 'form.html', data)

def login(request):
    data = {'form': loginform()}

    return render(request, 'login.html', data)

def register(request):
    data = {'form': registerform()}

    return render(request, 'register.html', data)

def test(request):
    data = {'form': testform()}

    return render(request, 'testpage.html', data)
