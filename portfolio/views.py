from django.shortcuts import render


def about(request):
    return render(request, 'about.html', {'title' : 'About'})

def welcome(request):
    return render(request, 'welcome_page.html')