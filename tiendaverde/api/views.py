from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import *

import os

# http response codes
# 200 = OK
# 403 = forbidden
# 404 = come on. you know what that one is
# 409 = conflict

# generate session token
def __gen_token():
    return os.urandom(16).hex()

# verify account
def __verify_account(request):
    # check if client token exists before indexing because otherwise it throws a fit like a baby
    server_token = user.objects.filter(session_token=request.session.get("token")) and user.objects.filter(session_token=request.session.get("token")).values()[0].get("session_token")
    local_token = request.session.get("token")

    # verify if token is valid
    return server_token and local_token and (server_token == local_token)

# Create your views here.

# for testing, might delete
def integer(request):
    print(request.POST)

    if(request.session.test_cookie_worked()):
        request.session.delete_test_cookie()
        return HttpResponse(status=200)

    return HttpResponse(status=404)

# not necessary according to specs so im leaving it as is
def recycle(request):
    print(request.POST)
    return HttpResponse(status=200)

def login(request):
    # reject request if no email is provided (probably vulnerable otherwise) or the password is wrong
    if(
        (not user.objects.filter(email=request.POST.get("email"))) or
        request.POST.get("password") != user.objects.get(email=request.POST.get("email")).password_sha256
    ):
       return HttpResponse(status=403)
    
    token = __gen_token()
    request.session["token"] = token

    session = user.objects.get(email=request.POST.get("email"))
    session.session_token = token
    session.save()

    return HttpResponse(status=200)

def register(request):
    print(request.POST)

    # reject request if user already exists
    if(user.objects.filter(email=request.POST.get("email"))):
        return HttpResponse(status=409)

    token = __gen_token()

    user(
        name=request.POST.get("name"), 
        email=request.POST.get("email"),
        password_sha256=request.POST.get("password"),
        session_token=token
    ).save()

    request.session["token"] = token

    return HttpResponse(status=200)

def logout(request):
    # must have a valid token to log in
    if(not __verify_account(request)):
        return HttpResponse(status=403)
    
    # delete tokens
    session = user.objects.get(session_token=request.session.get("token"))
    session.session_token = ""
    session.save()

    del request.session["token"]
    
    return HttpResponse(status=200)