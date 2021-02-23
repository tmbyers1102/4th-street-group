from django.shortcuts import render
from .models import Project, Screengrab, Requirement
from django.views.generic import DetailView


def home(request):
    context = {
        'projects': Project.objects.all(),
    }
    return render(request, 'web_app/home2.html', context)


def about(request):
    return render(request, 'web_app/about.html', {'title': 'About'})

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'web_app/project_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        context['screengrabs'] = Screengrab.objects.all()
        # In order to get just this project's requirements, we need to filter to just this project
        context['requirements'] = Requirement.objects.filter(assigned_project=str(Project.title))
        return context





