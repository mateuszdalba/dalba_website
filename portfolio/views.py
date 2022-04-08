from django.shortcuts import render
from django.http import HttpResponse
import random


def about(request):
    return render(request, 'about.html', {'title' : 'About'})

def welcome(request):
    return render(request, 'welcome_page.html')

def code_snippet(request):
    return render(request, 'code_snippets.html')

def cv(request):
    return render(request, 'cv.html')

def certificates(request):
    return render(request, 'certificates.html')

def notebook1(request): return render(request, 'notebook1.html')
def notebook2(request): return render(request, 'notebook2.html')
def notebook3(request): return render(request, 'notebook3.html')
def notebook4(request): return render(request, 'notebook4.html')
def notebook5(request): return render(request, 'notebook5.html')
def notebook6(request): return render(request, 'notebook6.html')
def notebook7(request): return render(request, 'notebook7.html')
def notebook8(request): return render(request, 'notebook8.html')



