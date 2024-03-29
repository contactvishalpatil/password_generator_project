from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    #return HttpResponse('Hello there Friend!')
    return render(request, 'generator/home.html')

def about(request):
    #return HttpResponse('Hello there Friend!')
    return render(request, 'generator/about.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%'))
    if request.GET.get('Numbers'):
        characters.extend(list('0987654321'))

    length = int(request.GET.get('length', 10))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password':thepassword} )