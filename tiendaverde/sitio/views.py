from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .forms import testform, recycle

# Create your views here.

def index(request):
    data = {}

    if request.POST:
        print(request.POST.get(''))

    return render(request, 'index.html', data)

def store(request):
    data = {}

    return render(request, 'store.html', data)

def form(request):
    data = {'form': recycle()}

    return render(request, 'form.html', data)

def test(request):
    data = {'form': testform()}

    return render(request, 'testpage.html', data)
