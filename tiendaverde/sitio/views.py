from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .forms import *

from api import models

# verify if session is valid
def __verify_account(request):
    # check if client token exists before indexing because otherwise it throws a fit like a baby
    server_token = models.user.objects.filter(session_token=request.session.get("token")) and models.user.objects.filter(session_token=request.session.get("token")).values()[0].get("session_token")
    local_token = request.session.get("token")

    return server_token and local_token and (server_token == local_token)

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
    if(not __verify_account(request)):
        return redirect("/login")

    data = {}

    return render(request, 'store.html', data)

def form(request):
    if(not __verify_account(request)):
        return redirect("/login")

    data = {'form': recycle()}

    return render(request, 'form.html', data)

def login(request):
    if(__verify_account(request)):
        return redirect("/account")

    data = {'form': loginform()}

    return render(request, 'login.html', data)

def register(request):
    data = {'form': registerform()}

    return render(request, 'register.html', data)

def account(request):
    data = {models.user.objects.filter(session_token=request.session.get("token")).values()[0]}

    return render(request, 'account.html', data)

# for testing
def test(request):
    data = {'form': testform()}

    return render(request, 'testpage.html', data)
