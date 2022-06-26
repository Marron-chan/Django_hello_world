from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def HelloWorldAppView(request):
    return HttpResponse('<h1>hello world app</h1>')
