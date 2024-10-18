from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def integer(request):
    print(request.POST)
    return HttpResponse(request.POST.get('value'))

def recycle(request):
    print(request.POST)
    return HttpResponse(request.POST.get('value'))