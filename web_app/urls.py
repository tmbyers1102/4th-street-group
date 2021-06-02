from django.urls import path
from . import views
from .views import ProjectDetailView, ContactCreateView

urlpatterns = [
    path('', views.home, name='web_app-home'),
    path('contact/', ContactCreateView.as_view(), name='web_app-contact'),
    path('<str:pk>/', ProjectDetailView.as_view(), name='project-details')
]
