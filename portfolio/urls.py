"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome_page'),
    path('admin/', admin.site.urls),
    path('projects/', include("projects.urls")),
    path('certificates/', views.certificates, name='certificates'),
    path('about/', views.about, name='about'),
    path('code_snippet/', views.code_snippet, name='code_snippet'),
    path('cv/', views.cv, name='cv'),
    path('notebook1', views.notebook1, name='notebook1'),
    path('notebook2', views.notebook2, name='notebook2'),
    path('notebook3', views.notebook3, name='notebook3'),
    path('notebook4', views.notebook4, name='notebook4'),
    path('notebook5', views.notebook5, name='notebook5'),
    path('notebook6', views.notebook6, name='notebook6'),
    path('notebook7', views.notebook7, name='notebook7'),
    path('notebook8', views.notebook8, name='notebook8'),
]
