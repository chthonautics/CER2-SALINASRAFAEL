from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def integer(request, id):
    print(request.POST.get('text'))
    return HttpResponse(request.POST.get('text'))