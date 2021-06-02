from django.shortcuts import render
from django.views import generic
from .models import Contact, Project, Screengrab, Requirement
from .forms import ContactModelForm
from django.views.generic import DetailView
from django.urls import reverse


def home(request):
    context = {
        'projects': Project.objects.all(),
    }
    return render(request, 'web_app/home2.html', context)


# def contact(request):
#     return render(request, 'web_app/contact.html', {'title': 'Contact'})


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


class ContactCreateView(generic.CreateView):
    template_name = "web_app/contact.html"
    model = Contact
    form_class = ContactModelForm

    def get_success_url(self):
        print('!!VIEWS!!: contact created')
        return reverse("web_app-home")


