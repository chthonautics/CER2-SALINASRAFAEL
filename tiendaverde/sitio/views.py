from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def index(request):
    data = {}

    return render(request, 'index.html', data)

def store(request):
    data = {}

    return render(request, 'store.html', data)

def form(request):
    data = {}

    return render(request, 'form.html', data)
