from re import X
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response
# Views in django : request handler

def calculate():
    x = 1
    y = 2
    return x

def say_hello(request):
    x = 1
    y = 2
    return render(request, 'hello.html', {'name' : 'Jaechul'})