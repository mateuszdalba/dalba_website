from django.shortcuts import render
from django.http import HttpResponse


def about(request):
    return render(request, 'about.html', {'title' : 'About'})

def welcome(request):
    return render(request, 'welcome_page.html')

def code_snippet(request):
    return render(request, 'code_snippets.html')

def cv(request):
    return render(request, 'cv.html')