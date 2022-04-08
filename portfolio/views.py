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

def notebook1(request):
    return render(request, 'notebook1.html')

def certificates(request):
    return render(request, 'certificates.html')