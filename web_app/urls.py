from django.urls import path
from . import views
from .views import ProjectDetailView

urlpatterns = [
    path('', views.home, name='web_app-home'),
    path('contact/', views.contact, name='web_app-contact'),
    path('<str:pk>/', ProjectDetailView.as_view(), name='project-details')
]
