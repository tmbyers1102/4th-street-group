from django.shortcuts import redirect, render, get_object_or_404
from django.views import generic
from .models import Contact, Project, Screengrab, Requirement, Log
from .forms import ContactModelForm
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


def home(request):
    context = {
        'projects': Project.objects.all().order_by('-date_posted'),
    }
    return render(request, 'web_app/home2.html', context)


def project_detail(request, pk):
    project_name = Project.objects.get(pk=pk)

    context = {
        'project': Project.objects.get(pk=pk),
        'project_logs': Log.objects.filter(project=project_name).order_by('-date_published'),
        'project_screengrabs': Screengrab.objects.filter(assigned_project=project_name),
    }
    return render(request, 'web_app/project_detail2.html', context)


# class ProjectDetailView(DetailView):
#     model = Project
#     template_name = 'web_app/project_detail.html'

#     def get_context_data(self, **kwargs):
#         # project_name = get_object_or_404(Project, title=self.kwargs.get('title'))
#         context = super().get_context_data(**kwargs)
#         context['projects'] = Project.objects.all()
#         context['screengrabs'] = Screengrab.objects.all()
#         # context['logs'] = Log.objects.filter(project=project_name).order_by('description')
#         # In order to get just this project's requirements, we need to filter to just this project
#         context['requirements'] = Requirement.objects.filter(assigned_project=str(Project.title))
#         return context


class ContactCreateView(SuccessMessageMixin, generic.CreateView):
    template_name = "web_app/contact.html"
    model = Contact
    form_class = ContactModelForm
    # success_url = reverse_lazy('users:login')
    success_message = "Thanks! We will be in touch!"

    def get_success_url(self):
        print('!!VIEWS!!: contact created')
        return reverse("web_app-home")

    # def success_message(request):
    #     messages.success(request, f'Contact Submitted! We will be in touch!')
    #     return reverse("web_app-home")





