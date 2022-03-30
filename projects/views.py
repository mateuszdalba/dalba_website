from django.shortcuts import render
from projects.models import Project
from .forms import ContactForm


def project_index(request):
    projects = Project.objects.all()

    context = {
        'projects':projects
    }

    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'projects':project
    }

    return render(request, 'project_detail.html', context)


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact_success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)
