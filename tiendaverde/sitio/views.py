from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .forms import *

from api import models

import json

# verify if session is valid
def __verify_account(request):
    # check if client token exists before indexing because otherwise it throws a fit like a baby
    server_token = models.user.objects.filter(session_token=request.session.get("token")) and models.user.objects.filter(session_token=request.session.get("token")).values()[0].get("session_token")
    local_token = request.session.get("token")

    return server_token and local_token and (server_token == local_token)

# Create your views here.

def index(request):
    data = {}

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
    if(not __verify_account(request)):
        return redirect("/login")
    
    session = models.user.objects.filter(session_token=request.session.get("token")).values()[0]

    cartData = []
    cart = json.loads(request.session.get("cart") or "[]")
    sum = 0

    for item in cart or []:
        itemData = models.product.objects.filter(name_id=item) and models.product.objects.filter(name_id=item).values()[0]

        cartData.append(itemData)
        sum += itemData["price"]

    data = {
        'name' : session.get("name"),
        'email': session.get("email"),
        'cart' : cartData,
        'total': sum
    }

    return render(request, 'account.html', data)
